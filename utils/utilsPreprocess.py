from transformers import WhisperTokenizer
from transformers import WhisperFeatureExtractor
from datasets import Dataset, DatasetDict
import pandas as pd
import wave
import numpy as np
import os
import shutil 

def process_transcript(file_path, audio_directory):
    # Read the file into a DataFrame
    df = pd.read_csv(
        file_path, sep="\t", header=None, names=["sentence_id", "sentence"]
    )

    # Fill NaN values in 'sentence_id' with the previous non-NaN value
    df["sentence_id"] = df["sentence_id"].fillna(method="ffill")

    # Convert 'sentence_id' to integer to remove decimal points
    df["sentence_id"] = df["sentence_id"].astype(int)

    # Group by 'sentence_id' and join the sentences
    df_grouped = df.groupby("sentence_id")["sentence"].apply(" ".join).reset_index()

    # Add a column for the audio file path
    df_grouped["audio_file"] = df_grouped["sentence_id"].apply(
        lambda x: os.path.join(audio_directory, f"{x}.WAV")
    )

    return df_grouped


def list_available_transcripts(transcript_base_directory):
    try:
        if os.path.exists(transcript_base_directory):
            # Case-insensitive check for .TXT files
            available_transcripts = [
                f
                for f in os.listdir(transcript_base_directory)
                if f.lower().endswith(".txt")
            ]
            return available_transcripts
        else:
            print(f"Directory not found: {transcript_base_directory}")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def process_speaker_transcripts(transcript_base_directory, audio_base_directory):
    dfs = []

    # List all transcript files available
    available_transcripts = [
        f for f in os.listdir(transcript_base_directory) if f.endswith(".txt")
    ]

    for transcript_file in available_transcripts:
        transcript_file_path = os.path.join(transcript_base_directory, transcript_file)

        # Extract speaker number and session number from transcript file name
        speaker_num = transcript_file[1:5]  # Second to fifth digit for speaker number
        session_num = transcript_file[5:6]  # Sixth digit for session number
        speaker_id = f"SPEAKER{speaker_num}"
        
        audio_directory_path = os.path.join(
            audio_base_directory, speaker_id, f"SESSION{session_num}"
        )

        if os.path.exists(audio_directory_path):
            print(f"Processing file: {transcript_file_path}")
            df = process_transcript(
                transcript_file_path, audio_directory_path
            )  # Assuming this function is already defined
            dfs.append(df)

            # Delete the transcript file after processing
            os.remove(transcript_file_path)
            print(f"Deleted processed file: {transcript_file}")
            
    if not dfs:
        print("No dataframes were created. No files were processed.")
        return None
    else:
        combined_df = pd.concat(dfs, ignore_index=True)
        print("Dataframes successfully concatenated.")
        return combined_df


def extract_speaker_and_session(transcript_file):
    # Implement the logic to extract speaker ID and session number from the transcript file name
    # Example: return "SPEAKER0001", "0" for a file named "200010.TXT"
    pass


def get_amplitude_array(file_path):
    with wave.open(file_path, "rb") as wave_file:
        assert (
            wave_file.getframerate() == 16000
        ), "Unexpected sampling rate in the audio file"
        raw_audio = wave_file.readframes(wave_file.getnframes())
        amplitude_array = np.frombuffer(raw_audio, dtype=np.int16)

        # Normalize and convert to float32
        amplitude_array = amplitude_array.astype(np.float32) / 32768.0
    os.remove(file_path)
    print(f"Deleted processed file: {file_path}")
    return amplitude_array


def prepare_dataset(batch):
    # load and resample audio data from 48 to 16kHz
    audio = batch["amplitude_array"]

    print("Initializing components for dataset preparation...")
    feature_extractor, tokenizer = initialize_components()
    print("Components initialized.")

    # compute log-Mel input features from input audio array
    batch["input_features"] = feature_extractor(
        audio, sampling_rate=16000
    ).input_features[0]

    # encode target text to label ids
    batch["labels"] = tokenizer(batch["sentence"]).input_ids
    return batch


def initialize_components():
    feature_extractor = WhisperFeatureExtractor.from_pretrained("openai/whisper-small")
    tokenizer = WhisperTokenizer.from_pretrained(
        "openai/whisper-small", language="English", task="transcribe"
    )
    return feature_extractor, tokenizer


def prepare_and_split_dataset(dataframe):
    dataframe["amplitude_array"] = dataframe["audio_file"].apply(get_amplitude_array)
    dataset = Dataset.from_pandas(dataframe)
    split_dataset = dataset.train_test_split(test_size=0.2)
    prepared_dataset = split_dataset.map(
        prepare_dataset, remove_columns=split_dataset.column_names["train"]
    )
    return prepared_dataset


def save_dataset(dataset, save_path):
    dataset.save_to_disk(save_path)


def load_dataset(load_path):
    return DatasetDict.load_from_disk(load_path)

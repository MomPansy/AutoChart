import dropbox
import pandas as pd
import argparse
import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from utils import utilsFiles, utilsPreprocess, utilsDropbox, DataProcessing

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('access_token', type=str, help='Dropbox access token')
    args = parser.parse_args()

    dbx = dropbox.Dropbox(args.access_token)
    print("Dropbox client initialized.")

    dropbox_folder_path = '/Test 20 speakers'
    script_folder_path = '/IMDA - National Speech Corpus/PART1/DATA/CHANNEL2/SCRIPT'
    transcript_base_directory = './SCRIPTS'
    audio_base_directory = './WAVE'

    print("Starting download of all transcripts...")
    utilsDropbox.download_all_files_in_folder(dbx, script_folder_path, transcript_base_directory)
    print("All transcripts downloaded.")

    batch_size = 2
    remaining_files = utilsDropbox.list_files(dbx, dropbox_folder_path)
    all_dfs = []

    while remaining_files:
        combined_df, remaining_files = DataProcessing.download_and_process_data(dbx, dropbox_folder_path, transcript_base_directory, audio_base_directory, batch_size, remaining_files)
        if combined_df is not None:
            all_dfs.append(combined_df)

    utilsFiles.remove_contents_of_directory(transcript_base_directory)
    final_df = pd.concat(all_dfs, ignore_index=True)

    print("Preparing and splitting dataset...")
    prepared_dataset = utilsPreprocess.prepare_and_split_dataset(final_df)

    utilsFiles.delete_directory(transcript_base_directory)
    utilsFiles.delete_directory(audio_base_directory)

    save_path = './preprocessed_data'
    utilsPreprocess.save_dataset(prepared_dataset, save_path)
    print(f"Dataset saved to {save_path}")

    google_drive_path = '/Users/jayden/Library/CloudStorage/GoogleDrive-jaydenyeo.acs@gmail.com/My Drive'
    save_path = os.path.join(google_drive_path, 'whisperfinetune_preprocessed_datav2')
    prepared_dataset.save_to_disk(save_path)

if __name__ == "__main__":
    main()

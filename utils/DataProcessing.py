from . import utilsDropbox
from . import utilsPreprocess

def download_and_process_data(dbx, folder_path, transcript_base_directory, audio_base_directory, batch_size, remaining_files):
    print(f"Downloading batch of files from {folder_path}...")
    remaining_files, downloaded_files = utilsDropbox.download_batch(dbx, folder_path, audio_base_directory, batch_size, remaining_files)

    if not downloaded_files:
        print("No more files to download.")
        return None, remaining_files

    print("Files downloaded. Starting processing...")
    combined_df = utilsPreprocess.process_speaker_transcripts(transcript_base_directory, audio_base_directory)
    return combined_df, remaining_files

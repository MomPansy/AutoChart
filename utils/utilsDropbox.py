import dropbox
import os
import zipfile
from tqdm import tqdm

def list_files(dbx, folder_path, batch_size=None):
    """
    List files in the given folder_path up to the specified batch_size.

    :param dbx: Dropbox client instance
    :param folder_path: Path to the folder in Dropbox
    :param batch_size: Maximum number of files to list (None for no limit)
    :return: List of file paths
    """
    try:
        file_paths = []
        result = dbx.files_list_folder(folder_path)

        while True:
            for entry in result.entries:
                if isinstance(entry, dropbox.files.FileMetadata):
                    file_paths.append(entry.path_lower)
                    if batch_size is not None and len(file_paths) >= batch_size:
                        return file_paths

            if not result.has_more:
                break

            result = dbx.files_list_folder_continue(result.cursor)

        return file_paths
    except dropbox.exceptions.ApiError as err:
        print(f"API Error: {err}")
        return []

def download_file(dbx, file_path, local_path):
    """
    Download a single file from Dropbox to local path.
    """
    try:
        dbx.files_download_to_file(local_path, file_path)
    except dropbox.exceptions.ApiError as err:
        print(f"Failed to download {file_path}: {err}")

def download_all_files_in_folder(dbx, folder_path, local_directory):
    """
    Download all files from a Dropbox folder to a local directory.

    :param dbx: Dropbox client instance
    :param folder_path: Path to the folder in Dropbox
    :param local_directory: Local directory to save files
    """
    # Ensure local directory exists
    if not os.path.exists(local_directory):
        os.makedirs(local_directory)

    # List all files in the Dropbox folder
    file_paths = list_files(dbx, folder_path)

    # Download each file with a progress bar
    for file_path in tqdm(file_paths, desc="Downloading files"):
        local_file_path = os.path.join(local_directory, os.path.basename(file_path))
        download_file(dbx, file_path, local_file_path)

def download_batch(dbx, folder_path, dir, batch_size, remaining_files):
    if not os.path.exists(dir):
        os.makedirs(dir)

    downloaded_files = []
    
    # Use tqdm to create a progress bar
    for _ in tqdm(range(min(batch_size, len(remaining_files))), desc="Downloading batch"):
        if remaining_files:
            file_path = remaining_files.pop(0)  # Get the next file to download
            local_file_path = os.path.join(dir, os.path.basename(file_path))
            download_file(dbx, file_path, local_file_path)

            # Check and extract zip file
            if zipfile.is_zipfile(local_file_path):
                with zipfile.ZipFile(local_file_path, "r") as zip_ref:
                    zip_ref.extractall(dir)
                os.remove(local_file_path)

            downloaded_files.append(local_file_path)

    return remaining_files, downloaded_files

def process_files(file_paths):
    """
    Process each file in the given list of file paths.
    """
    for file_path in file_paths:
        # Implement your processing logic here
        print(f"Processing {file_path}")

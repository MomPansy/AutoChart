import os
import shutil

def remove_contents_of_directory(directory):
    if os.path.exists(directory):
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        print(f"All files and folders within {directory} have been removed.")
    else:
        print(f"The directory {directory} does not exist.")

def delete_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
        print(f"Deleted directory: {directory}")
    else:
        print(f"The directory {directory} does not exist.")

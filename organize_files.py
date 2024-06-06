import os
import shutil
import json
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(filename='file_organizer.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Load configuration from JSON file
with open('config.json') as config_file:
    config = json.load(config_file)

desktop_path = os.path.expanduser(config["desktop_path"])
custom_folders = config["custom_folders"]

# Create custom folders if they don't exist
def create_folders():
    for folder_name in custom_folders.keys():
        folder_path = os.path.join(desktop_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)

# Move files to respective custom folders based on file type
def move_files_to_custom_folders():
    for file in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            for folder_name, extensions in custom_folders.items():
                if file_ext in extensions or not extensions:
                    try:
                        dest = os.path.join(desktop_path, folder_name, file)
                        if os.path.exists(dest):
                            dest = os.path.join(desktop_path, folder_name, f"{os.path.splitext(file)[0]}_{int(datetime.timestamp(datetime.now()))}{file_ext}")
                        shutil.move(file_path, dest)
                        logging.info(f"Moved file {file} to {folder_name}")
                    except Exception as e:
                        logging.error(f"Error moving file {file}: {e}")
                    break

def sort_files_by_mod_date():
    # Create a folder for sorted files
    sorted_folder = os.path.join(desktop_path, "Sorted Files")
    os.makedirs(sorted_folder, exist_ok=True)
    for file in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, file)
        # Sort files into folders by modification date
        if os.path.isfile(file_path):
            try:
                mod_time = os.path.getmtime(file_path)
                mod_date = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d")
                dest_folder = os.path.join(sorted_folder, mod_date)
                os.makedirs(dest_folder, exist_ok=True)
                dest_file = os.path.join(dest_folder, file)
                if os.path.exists(dest_file):
                    dest_file = os.path.join(dest_folder, f"{os.path.splitext(file)[0]}_{int(datetime.timestamp(datetime.now()))}{os.path.splitext(file)[1]}")
                shutil.move(file_path, dest_file)
                logging.info(f"Moved file {file} to {dest_folder}")
            except Exception as e:
                logging.error(f"Error sorting file {file} by date: {e}")

if __name__ == "__main__":
    try:
        create_folders()
        move_files_to_custom_folders()
        sort_files_by_mod_date()
        logging.info("File organization completed successfully.")
    except Exception as e:
        logging.critical(f"Critical error during file organization: {e}")
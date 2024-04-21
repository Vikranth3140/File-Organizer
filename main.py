import os
import shutil
from datetime import datetime

# Replace "C:\Users\vikra\OneDrive\Desktop" with your own Absolute File Path
desktop_path = os.path.expanduser(r"C:\Users\vikra\OneDrive\Desktop")

# Create a dictionary of custom folders and their corresponding file extensions
custom_folders = {
    "Photos": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".doc", ".docx", ".txt", ".pdf"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Code": [".py", ".cpp", ".java", ".sh"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".msi"],
    "Others": []  # Add any other file extensions you want to handle separately
}

# Create custom folders if they don't exist
for folder_name, extensions in custom_folders.items():
    folder_path = os.path.join(desktop_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)

# Move files to respective custom folders based on file type
for file in os.listdir(desktop_path):
    if os.path.isfile(os.path.join(desktop_path, file)):
        file_ext = os.path.splitext(file)[1].lower()
        for folder_name, extensions in custom_folders.items():
            if file_ext in extensions:
                src = os.path.join(desktop_path, file)
                dest = os.path.join(desktop_path, folder_name, file)
                shutil.move(src, dest)
                break

# Create a folder for sorted files
sorted_folder = os.path.join(desktop_path, "Sorted Files")
os.makedirs(sorted_folder, exist_ok=True)

# Sort files into folders by modification date
for file in os.listdir(desktop_path):
    if os.path.isfile(os.path.join(desktop_path, file)):
        file_path = os.path.join(desktop_path, file)
        mod_time = os.path.getmtime(file_path)
        mod_date = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d")
        dest_folder = os.path.join(sorted_folder, mod_date)
        os.makedirs(dest_folder, exist_ok=True)
        dest_file = os.path.join(dest_folder, file)
        shutil.move(file_path, dest_file)
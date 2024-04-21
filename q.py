import os
import shutil

# Replace "C:\Users\vikra\OneDrive\Desktop" with your own Absolute File Path
desktop_path = os.path.expanduser(r"C:\Users\vikra\OneDrive\Desktop")

# Create folders for different file types
folders = {
    "Documents": [".doc", ".docx", ".txt", ".pdf"],
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".msi"],
    "Scripts": [".py", ".sh"]
}

# Create folders if they don't exist
for folder_name in folders:
    folder_path = os.path.join(desktop_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)

# Move files to respective folders
for file in os.listdir(desktop_path):
    if os.path.isfile(os.path.join(desktop_path, file)):
        file_ext = os.path.splitext(file)[1].lower()
        for folder_name, extensions in folders.items():
            if file_ext in extensions:
                src = os.path.join(desktop_path, file)
                dest = os.path.join(desktop_path, folder_name, file)
                shutil.move(src, dest)
                break
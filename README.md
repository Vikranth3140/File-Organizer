# File Organizer

File Organizer is a Python script designed to organize files on your desktop by moving them into custom folders based on their file types and sorting them by modification date. The script also backs up files before moving them to ensure data safety.

## Features

- **Custom Folders**: Automatically creates and organizes files into user-defined folders based on file extensions.
- **Backup**: Backs up files before moving them to ensure data safety.
- **Sorting**: Sorts files by modification date into dated folders.
- **Configuration**: Allows custom configuration via a JSON file.
- **Command-Line Arguments**: Supports passing custom paths and configuration files as command-line arguments.
- **Logging**: Logs all activities and errors for easy debugging and tracking.

## How to Use

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Vikranth3140/File-Organizer.git
    cd File-Organizer
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

Create a `config.json` file in the root directory with the following structure:

```json
{
    // # Replace "C:\Users\vikra\OneDrive\Desktop" with your own Absolute File Path
    "desktop_path": "C:\\Users\\YourUsername\\Desktop",
    "custom_folders": {
        "Photos": [".png", ".jpg", ".jpeg", ".gif"],
        "Documents": [".doc", ".docx", ".txt", ".pdf"],
        "Music": [".mp3", ".wav"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Code": [".py", ".cpp", ".java", ".sh"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Executables": [".exe", ".msi"],
        "Others": [] // Add any other file extensions you want to handle separately
    },
    "ignore_files": ["file_organizer.log", "config.json"]
}
```

### Running the Script

Run the script using Python:

```bash
python file_organizer.py --config config.json
```

### Command-Line Arguments

- `--config`: Path to the configuration file (default: `config.json`).

## Folder Structure

The script organizes files into the following structure:

```
Desktop/
├── Backup/
│   └── yourfile.txt
├── Photos/
│   └── image.png
├── Documents/
│   └── document.pdf
├── Music/
│   └── song.mp3
├── Videos/
│   └── movie.mp4
├── Code/
│   └── script.py
├── Archives/
│   └── archive.zip
├── Executables/
│   └── installer.exe
└── Sorted Files/
    └── 2023-12-31/
        └── oldfile.txt
```

## Logging

All activities and errors are logged in `file_organizer.log`:

```
2024-06-07 10:00:00 - INFO - Backed up file yourfile.txt to Backup folder
2024-06-07 10:00:01 - INFO - Moved file yourfile.txt to Documents
2024-06-07 10:00:02 - INFO - File organization completed successfully.
```

## License

This project is licensed under the [MIT License](LICENSE).
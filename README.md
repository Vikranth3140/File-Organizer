# File Organizer

This Python script organizes files on your desktop based on their file types and modification dates.

## Features

- Organizes files into predefined folders based on file types such as documents, images, videos, music, code, archives, executables, and others.
- Creates custom folders for specific file extensions according to user-defined preferences.
- Sorts files into subfolders within a "Sorted Files" folder based on their modification dates.

## How to Use

1. Clone or download the project repository.
    ```bash
    git clone https://github.com/your-username/file-organizer.git
    ```

2. Open the `organize_files.py` script in a text editor.
3. Update the `desktop_path` variable with your desktop's absolute file path.
4. Customize the `custom_folders` dictionary to include your preferred folder names and file extensions.
5. Run the script.
    ```bash
    python organize_files.py
    ```

## Folder Structure

After running the script, your desktop will have the following structure:

```
- Documents
- Images
- Videos
- Music
- Code
- Archives
- Executables
- Others
- Sorted Files
  - YYYY-MM-DD (sorted files by modification date)
```

## License

This project is licensed under the MIT License - see the [MIT LICENSE](LICENSE) file for details.
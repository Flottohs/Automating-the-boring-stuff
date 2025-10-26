from pathlib import Path as p
import os
import zipfile

def backup_to_zip(folder):
    folder = p(folder)  # ensure it's a Path object
    
    if not folder.exists() or not folder.is_dir():
        print(f"Error: {folder} does not exist or is not a directory.")
        return
    
    # Find next available ZIP filename
    num = 1
    while True:
        zipfile_name = folder.parent / f"{folder.name}_{num}.zip"
        if not zipfile_name.exists():
            break
        num += 1

    print(f"Creating {zipfile_name}...")

    # Create the ZIP file
    with zipfile.ZipFile(zipfile_name, 'w') as backup_zip:
        for folder_name, subfolders, filenames in os.walk(folder):
            folder_name = p(folder_name)
            
            # Skip any virtual environment folders
            if '.venv' in folder_name.parts:
                continue
            
            print(f"Adding files from {folder_name}...")
            for filename in filenames:
                file_path = folder_name / filename
                arcname = file_path.relative_to(folder)
                backup_zip.write(file_path, arcname=arcname)
                print(f"Added: {arcname}")
    
    print(f"Backup complete! ZIP created at: {zipfile_name}")

user_folder = input("Enter the full path of the folder to back up: ")
backup_to_zip(user_folder)

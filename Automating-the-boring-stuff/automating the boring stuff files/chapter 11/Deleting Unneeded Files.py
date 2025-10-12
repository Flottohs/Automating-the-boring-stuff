'''It’s not uncommon for a few unneeded but humongous files or folders to take up the bulk of the space on your hard drive. If you’re trying to free up room on your computer, it’s more effective to identify the largest unneeded files first.

Write a program that walks through a folder tree and searches for exceptionally large files or folders—say, ones that have a file size of more than 100MB. (Remember that, to get a file’s size, you can use os.path.getsize() from the os module.) Print these files with their absolute path to the screen.'''
import os
from pathlib import Path

def storage_sweeper(folder):
    
    folder = Path(folder)
    if  not folder.exists():
        print(f"folder {folder}, does not exist")
        return
    
    large_files = {}

    
    for folder_name, subfolders, filenames in os.walk(folder):
        
        for filename in filenames:
            file_path = Path(folder_name) / filename
            filesize = os.path.getsize(file_path) 
            if filesize >  1 * 1024 * 1024:
                large_files[file_path] = filesize
                
                
    if not large_files:
        print("no large files")
    else:
        
        for k, v in large_files.items():
            print(f"You have a large file named{k}, with a file size of {v} bytes ")

            
    

        
    
                
                
                
        
        
    
    
    
    
    
    
    
    
    
    
    
print("input folder name")
folder = input()
storage_sweeper(folder)
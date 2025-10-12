#Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). Copy these files from their current location to a new folder.


from pathlib import Path
import os
import glob
import shutil
#creating function

def copy_file(folder,criteria):
    new_folder = Path('new_folder')
    new_folder.mkdir(exist_ok=True)
    
    
    for folder_name , subfolder, filenames in os.walk(folder):
        folder_name = Path(folder_name)
        passed = list(folder_name.glob(criteria))
        for i in range(len(passed)):
            shutil.copy2(passed[i], new_folder / passed[i].name)

    
    
    
print("input foldername")
foldername = input()
    
print("what would you like your criteia to be?")
criteria = input()
    
copy_file(Path.home() / foldername, criteria )
'''
Say your boss emails you thousands of files with American-style dates (MM-DD-YYYY) in their names and needs them renamed to European-style dates (DD-MM-YYYY). This boring task could take all day to do by hand! Instead, write a program that does the following:

  1.  Searches all filenames in the current working directory and all subdirectories for American-style dates. Use the os.walk() function to go through the subfolders.

  2.  Uses regular expressions to identify filenames with the MM-DD-YYYY pattern in them—for example, spam12-31-1900.txt. Assume the months and days always use two digits, and that files with non-date matches don’t exist. (You won’t find files named something like 99-99-9999.txt.)

  3.  When a filename is found, renames the file with the month and day swapped to make it European-style. Use the shutil.move() function to do the renaming.

'''
import os
import re
import shutil
from pathlib import Path

def euro_converter(folder):
    folder_path = Path(folder)
    american_re = re.compile(r'(.*?)(\d{2})-(\d{2})-(\d{4})(.*)')

    for folder_names, subfolders, filenames in os.walk(folder_path):
        folder_path_current = Path(folder_names)
        for filename in filenames:
            match = american_re.match(filename)
            if match:
                prefix, month, day, year, suffix = match.groups()
                new_filename = f"{prefix}{day}-{month}-{year}{suffix}"
                old_path = folder_path_current / filename
                new_path = folder_path_current / new_filename
                if not new_path.exists():
                    print(f"Renaming {old_path} → {new_path}")
                    shutil.move(old_path, new_path)
                else:
                    print(f"Skipped {new_path}, file already exists!")

folder = input("Input folder name: ")
euro_converter(folder)
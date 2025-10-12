# ---------------------------
# shutil module
# ---------------------------
# allows you to copy, move, rename, and delete files or folders in python.
# stands for "shell utilities"

# from pathlib import Path
# import shutil
# import os
# import send2trash
# import zipfile

# h = Path.home()


# ---------------------------
# making directories
# ---------------------------

# mkdir = make directory
# exist_ok=True → doesn't error if folder already exists
# (h / 'spam').mkdir(exist_ok=True)

# creating files
# with open(h / 'spam/file1.txt', 'w', encoding='utf-8') as file:
#     file.write('hello world')


# ---------------------------
# copying files and folders
# ---------------------------

# copy file to home directory
# shutil.copy(h / 'spam/file1.txt', h)

# copy file with new name
# shutil.copy(h / 'spam/file1.txt', h / 'spam/file2.txt')

# copy an entire folder and all its contents
# shutil.copytree(h / 'spam', h / 'spam_backup')


# ---------------------------
# moving and renaming
# ---------------------------

# move a file into another folder
# (h / 'spam2').mkdir(exist_ok=True)
# shutil.move(h / 'spam/file1.txt', h / 'spam2')

# rename while moving
# shutil.move(h / 'spam2/file1.txt', h / 'spam2/new_name.txt')

# if destination doesn’t exist, shutil.move() renames the file


# ---------------------------
# deleting files and folders
# ---------------------------

# permanently remove an entire folder tree
# shutil.rmtree(path)

# permanently remove a single file
# os.unlink(path)

# permanently remove an empty folder
# os.rmdir(path)

# example: delete all .txt files in home (be careful!)
# for filename in Path.home().glob('*.txt'):
#     os.unlink(filename)

# safer deletion (sends to recycle bin)
# send2trash.send2trash('file1.txt')


# ---------------------------
# walking a directory tree
# ---------------------------

# list all files/folders in a single directory
# os.listdir(h)

# list all path objects in a folder
# list(h.iterdir())

# create a sample folder structure
# (h / 'spam').mkdir(exist_ok=True)
# (h / 'spam/eggs').mkdir(exist_ok=True)
# (h / 'spam/eggs2').mkdir(exist_ok=True)
# (h / 'spam/eggs/bacon').mkdir(exist_ok=True)

# for f in [
#     'spam/file1.txt',
#     'spam/eggs/file2.txt',
#     'spam/eggs/file3.txt',
#     'spam/eggs/bacon/file4.txt'
# ]:
#     with open(h / f, 'w', encoding='utf-8') as file:
#         file.write('Hello')

# structure created:
# home/spam/
# ├── file1.txt
# ├── eggs/
# │   ├── file2.txt
# │   ├── file3.txt
# │   └── bacon/
# │       └── file4.txt
# └── eggs2/


# ---------------------------
# walking directory trees with os.walk()
# ---------------------------

# os.walk() iterates through every folder, subfolder, and file
# returns: (folder_name, subfolders, filenames)

# for folder_name, subfolders, filenames in os.walk(h / 'spam'):
#     print(f"current folder: {folder_name}")
#     for subfolder in subfolders:
#         print(f"subfolder of {folder_name}: {subfolder}")
#     for filename in filenames:
#         print(f"file inside {folder_name}: {filename}")

#         # example: rename each file to uppercase
#         p = Path(folder_name)
#         shutil.move(p / filename, p / filename.upper())
#     print('')


# ---------------------------
# working with zip files
# ---------------------------

# creating a zip file
# with zipfile.ZipFile('example.zip', 'w') as example_zip:
#     example_zip.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

# note:
# 'w' mode overwrites existing zips
# use 'a' mode to append new files instead
# compresslevel=9 = slowest but most compressed (default is 6)


# ---------------------------
# reading zip files
# ---------------------------

# example_zip = zipfile.ZipFile('example.zip')
# print(example_zip.namelist())  # list of files inside zip

# file1_info = example_zip.getinfo('file1.txt')
# print(file1_info.file_size)
# print(file1_info.compress_size)

# print(f"compressed file is {round(file1_info.file_size / file1_info.compress_size, 2)}x smaller!")

# example_zip.close()


# ---------------------------
# extracting zip files
# ---------------------------

# example_zip = zipfile.ZipFile('example.zip')
# example_zip.extractall()  # extracts all contents to current directory
# example_zip.close()
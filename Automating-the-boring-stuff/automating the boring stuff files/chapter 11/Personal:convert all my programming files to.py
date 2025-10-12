#must go through programming  folder and its subfolders and convert all non extension files to .py files


import shutil
import os
from pathlib import Path
import re
def convert_all_programming_files_to_py(programming):
    check_re = re.compile(r'^(?!.*\.).+$') 
    programming_path = Path(programming)
    for folder_name, subfolders, filenames in os.walk(programming_path):
        for filename in filenames:
            match = check_re.search(filename)
            if match:
                file_path = Path(folder_name) / filename
                new_name= filename + '.py'
                new_path = Path(folder_name) / Path(new_name)
                shutil.move(file_path , new_path )
            
convert_all_programming_files_to_py('/Users/haydenfletcher/Documents/programming')
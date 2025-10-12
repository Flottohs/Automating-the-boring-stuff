'''Renumbering Files
Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and a spam003.txt but no spam002.txt). Have the program rename all the later files to close this gap.

To create these example files (skipping spam042.txt, spam086.txt, and spam103.txt), run the following code:

>>> for i in range(1, 121):
...     if i not in (42, 86, 103):
...         with open(f'spam{str(i).zfill(3)}.txt', 'w') as file:
...             pass
...
As an added challenge, write another program that can insert gaps into numbered files (and bump up the numbers in the filenames after the gap) so that a new file can be inserted.

'''



import shutil
import os
from pathlib import Path
import re



def search(folder, prefix):
    folder_path = Path(folder) #convert the path(which was a string) to a path format

    check_re = re.compile(rf'({prefix})(\d+)(?:{re.escape('.txt')})')#checking for files with the correct format
    #setting variables
    passednum = []
    passedsec1 = []
    passedsec3 = []
    full_paths = []

    #filetree walking
    for folder_name, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            folder = Path(folder_name)
            
        
            
            match = check_re.search(filename)
            if match:
                passedsec1.append(match.group(1))
                passednum.append(int(match.group(2)))
                passedsec3.append(match.group(3))
                full_paths.append(folder / filename)
                
                

            
                
    combined = list(zip(passednum, passedsec1, passedsec3, full_paths)) #combining the num , both sections, and the full path into one list of touples
    combined.sort(key=lambda x: x[0])  #organizing the number in the front
                
    new_paths = []
    for index , (num, sec1, sec3, path) in enumerate(combined, start = 1):# re naming based on order
        new_name = f"{sec1}{str(index).zfill(3)}{sec3}" #must use index of the enumerate, as it gives the updated number, ifused num, no gaps would be closed
        new_path = path.parent / new_name
        new_paths.append(new_path)
        
        
    for old_path , new_path in zip (full_paths, new_paths):
        if old_path  != new_path:
            print(f"renaming{old_path.name} - > {new_path.name}")
            shutil.move(old_path, new_path)

   
    
    
        
        

        
    

    
print("input folder path")
folder = input()
prefix = input("input prefix")
search(folder,prefix)
'''Say you’re working on a project whose files you keep in a folder named C:\Users\Al\AlsPythonBook. You’re worried about losing your work, so you’d like to create ZIP file “snapshots” of the entire folder. You’d also like to keep different versions of these snapshots, so you want the ZIP file’s filename to increment each time a new version is made; for example, AlsPythonBook_1.zip, AlsPythonBook_2.zip, AlsPythonBook_3.zip, and so on. You could do this by hand, but that would be rather annoying, and you might accidentally misnumber the ZIP files’ names. It would be much simpler to run a program that does this boring task for you.

For this project, open a new file editor window and save it as backup_to_zip.py.'''


from pathlib import Path as p, os, zipfile






def backup_to_zip(folder):
    
    folder = p(folder)#makes sure its a path object nt a string + it gets the absolute path of the 'folder'
    
    num = 1
    while True:
        #loops through, updates the correct zipfile name that it should have, adds the folders parts with _ , the increment, and .zip to make it a zipfile
        zipfile_name = p(folder.parts[-1] + '_' + str(num) + '.zip')
        #breaks if this zipfile hasnt been made before, which means the new zipfile will start at this increment. The code will only work if either the user hasnt made a zipfile yet, or they havee the same formatting for the zipfile.
        if  not zipfile_name.exists():
            break
        num +=1
        

        
        
        #creating zip files
        
        print(f'Creating {zipfile_name}...')
        backup_zip = zipfile.ZipFile(zipfile_name, 'w')
        
        #now that we have created the new file, we can walk through the folder, and add the full directory, and its subfolders and files into this zipfile
        
        for folder_name, subfolders, filenames in os.walk(folder):
            folder_name = p(folder_name)
            print(f"adding files from {folder_name}, to {zipfile_name}...")
            for filename in filenames:
                print(f"adding file{filename}")
                backup_zip.write(folder_name / filename)#backup_zip.write(folder_name / filename, arcname=(folder_name / filename).relative_to(folder))
        backup_zip.close()
        print("done!")
            

        
        
        #if you want to keep the structure use: backup_zip.write(folder_name / filename, arcname=(folder_name / filename).relative_to(folder))
        #this code creates the zip with the folder, and all the files inside the folder, it lost the structure with having subfolders, but still works
        
        
backup_to_zip(p.home() / 'spam')        
        
        
        
        
        
        
        
    


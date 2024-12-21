"""
PATHLIB: pathlib is a python library and can be seen as a substitute to the os library. pathlib
         uses a path object path to represent file paths. using pathlib also gives you the ability to use its functions
         (since it is a class and has its own member functions) such as .exists(), etc.

         a total list of functions that can be used can be seen with dir(Path) command after importing Path from pathlib 

in this file we are renaming files based on the parent folder's name.    

docs: https://docs.python.org/3/library/pathlib.html
"""

from pathlib import Path

root_dir = Path('files')
print(root_dir)

file_paths = root_dir.glob("**/*")                         #we are instructing python to go into folders and their subfolders.
print(file_paths)

for path in file_paths:
    if path.is_file():                                     #normally glob would print out both the folders and the things inside the folders. but here we are saying just print out the files, not the folders too
        parent_folder = path.parts[-2]                     #getting the name of the folder in which the file is currently in. .parts() will create a list of the directory, so ('files', 'November', 'abc.txt') for example. since 'abc.txt' is at index -1, and the folder is directly behind the file, we use index -2 to grab the folder name.
        new_file_name = parent_folder + "-" + path.name    
        new_file_path = path.with_name(new_file_name)
        path.rename(new_file_path)
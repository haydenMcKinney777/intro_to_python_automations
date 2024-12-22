"""
Create empty files
"""
from pathlib import Path

root_directory = Path('files')


for i in range(10,21):
    file_name = (f"{i}.txt")
    file_path = root_directory / Path(file_name)    #'/' combines the two path objects into a single path
    file_path.touch()                               #creates the file. if it already exists, it does nothing
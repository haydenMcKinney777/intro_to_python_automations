"""
Create archive from files - i.e. grab all files in a folder and put them into a .zip file
"""
from pathlib import Path
import zipfile

root_directory = Path('files')

archive_path = root_directory / Path('archive.zip')     #we know that we want to have a zip folder that will contain all of our files, so we are constructing a path that describes where we want this file to be

with zipfile.ZipFile(archive_path, 'w') as zf:
    for path in root_directory.rglob('*.txt'):          #recursively search through all folders and subfolders, only grabbing the .txt files
        zf.write(path)                                  #add the file at 'path' to the zip archive. if our file structure is (files / subfolder / text.txt) and we said zf.write(path), then 'subfolder / text.txt' would go inside the zip file since file structure is preserved. if we want just the file without the parent folders, research 'arcname'
        path.unlink()                                   #deletes a file object. in our case, after we move the file into the zip archive file, we delete it from our directory
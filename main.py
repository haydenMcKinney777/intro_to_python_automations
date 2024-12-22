"""
Extract zip files into folders. we want to take archive.zip and archive2.zip, take all their contents
out, and place them into folders that mirror the .zip files name's.
"""

from pathlib import Path
import zipfile

root_directory = Path('.')                                    #we are not working inside any particular folder - we're working in the base directory that the script is located inside of. 
destination_path = root_directory / Path('archive_folders')

for path in root_directory.glob('*.zip'):                     #find and work with all .zip files
    with zipfile.ZipFile(path, 'r') as zf:
        final_path = destination_path / Path(path.stem)
        zf.extractall(final_path)
    path.unlink()                                             #delete the zip file from current directory after moving its contents into its own folder.

"""
the lines below will take any .txt files you have and put them into a .zip file.

for path in root_directory.rglob('*.txt'):
    with zipfile.ZipFile('archive.zip', 'w') as zf:
        zf.write(path)
        path.unlink()

"""
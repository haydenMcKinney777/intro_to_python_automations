"""
Exercise5: search for files on your computer given a search term
"""
from pathlib import Path
root_directory = Path('files')

for path in root_directory.glob("**/*"):
    for i in range(10,21):
        destination_path = root_directory / Path(f"{i}.txt")
        path.


# search_term = input("Enter search term for file: ")
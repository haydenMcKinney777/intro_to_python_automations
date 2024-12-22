"""
Exercise5: search for files on your computer given a search term

this exercise is set up in a way that there are multiple .txt files with '14' found in them.
"""
from pathlib import Path
root_directory = Path('files')

search_term = input("Enter search term for file: ")

for path in root_directory.rglob('*.txt'):
    if path.is_file():
        if search_term in path.stem:
            print(path.absolute())


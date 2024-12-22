"""
Exercise3: change all file extensions in a folder to .csv

"""

from pathlib import Path

root_directory = Path("files")

for path in root_directory.rglob("*.txt"):
    if path.is_file():
        new_file_path = path.with_suffix(".csv")
        path.rename(new_file_path)
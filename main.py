"""
Extract zip files into folders
"""

from pathlib import Path
import zipfile

root_directory = Path('.')

for path in root_directory.glob('*.txt'):
    with zipfile.ZipFile('archive2.zip', 'w') as zf:
        zf.write(path)
        path.unlink()
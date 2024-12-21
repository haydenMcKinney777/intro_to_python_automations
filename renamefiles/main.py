"""
Exercise3: add created date to all filenames in folder

"""

from pathlib import Path
from datetime import datetime

root_directory = Path("files")

for path in root_directory.glob("**/*"):
    if path.is_file():
        created_time_seconds = datetime.fromtimestamp(path.stat().st_birthtime)          #path.stat() gives us statistics about the file, such as when it was created. st_birthtime is that time (in timestamp format, not string)
        created_time_date = created_time_seconds.strftime("%Y-%m-%d_%H-%M-%S")           #in order to append the date and time to our file names it needs to be converted into a string using .strftime()
        path_parts = path.parts[1:]
        new_file_name = created_time_date + "-" + ("-".join(path_parts))
        new_file_path = path.with_name(new_file_name)
        path.rename(new_file_path)
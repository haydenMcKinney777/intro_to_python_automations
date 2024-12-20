"""
PATHLIB: pathlib is a python library and can be seen as a substitute to the os library. pathlib
         uses a path object path to represent file paths. using pathlib also gives you the ability to use its functions
         (since it is a class and has its own member functions) such as .exists(), etc.

         a total list of functions that can be used can be seen with dir(Path) command after importing Path from pathlib 

        in this file we are taking some directory with files in it, and adding a prefix to all the filenames inside that directory.
                  
"""

from pathlib import Path

p1 = Path("./files/ghi.txt")
if not p1.exists():
    with open(p1, "w") as file:
        file.write("Content 6")

print(p1.name)
print(p1.stem)
print(p1.suffix)

root_dir = Path('files')
file_paths = root_dir.iterdir()

for path in file_paths:
    new_filename = "new-" + path.stem + path.suffix         #since we are using pathlib, we are able to split each file name up into its stem and suffix. With this, we can append words such as "new-" to the beginning of the filename, ultimately renaming the file
    new_filepath = path.with_name(new_filename)             #with_name() ensures you're renaming the file in the same directory where the original file resides, avoiding accidental moves to a different directory.
    path.rename(new_filepath)   
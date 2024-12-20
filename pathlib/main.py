"""
PATHLIB: pathlib is a python library and can be seen as a substitute to the os library. pathlib
         uses a path object path to represent file paths. using pathlib also gives you the ability to use its functions
         (since it is a class and has its own member functions) such as .exists(), etc.

         a total list of functions that can be used can be seen with dir(Path) command after importing Path from pathlib 
"""

from pathlib import Path

p1 = Path("./files/ghi.txt")

if not p1.exists():
    with open(p1, "w") as file:
        file.write("Content 6")

print(p1.name)
print(p1.stem)
print(p1.suffix)

p2 = Path('files')
print(type(p2))

for item in p2.iterdir():               #p2.iterdir() is used to iterate over the files and directories within a directory
    print(item)                         #p2 points to the 'files' folder, so p2.iterdir() would be everything inside the files folder.
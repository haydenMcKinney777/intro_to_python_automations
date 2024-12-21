"""
Exercise2: Rename all files based on "sub-sub-folders"

"""

from pathlib import Path

root_directory = Path('files')

for path in root_directory.glob('**/*'):
    if path.is_file():                                                                          #we only want files. .glob() will list every single directory, we don't want that.
        subfolders = path.parts[1:-1]           #from the first index (which is the first subfolder inside the "files" folder) to the -1 index which is the file.
        print(subfolders)
        new_file_name = "-".join(subfolders) + "-" + path.name      #.joins() method will take 'subfolders' and separate each thing in the 'subfolders' tuple by a '-'. this makes it so that any subfolder path no matter how deep will correctly be separated with a dash.
        new_path_name = path.with_name(new_file_name)               #this line is needed because if we were to just say path.rename(new_file_name) the renamed files would not be placed in their original folders.
        path.rename(new_path_name)
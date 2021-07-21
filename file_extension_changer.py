import os
from pprint import pprint

file_loc = input('Enter folder location where the file is located: ')

pprint('Path: {}' . format(file_loc))
print()

old_extension = '.' + input('Enter old file extension (eg. txt, mp3, mp4) : ')
new_file_extension = '.' + input('Enter new file extension (eg. txt, mp3, mp4) : ')

counter = 0

with os.scandir(file_loc) as file_and_folders:
    for element in file_and_folders:
        if element.is_file():
            root, ext = os.path.splitext(element.path)
            if ext == old_extension:
                new_path = root + new_file_extension
                os.rename(element.path, new_path)
                counter += 1

pprint('Number of files processed: {}' . format(counter))
pprint('file extension was changed from {} to {}' . format(old_extension, new_file_extension))
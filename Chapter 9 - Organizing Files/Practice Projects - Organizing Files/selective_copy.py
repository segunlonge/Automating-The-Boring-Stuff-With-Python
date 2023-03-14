'''Write a program that walks through a folder tree and searches
for files with a certain file extension (such as .pdf or .jpg).
Copy these files from whatever location they are in to a new folder.

Use .txt files for this project
'''

import os, re, shutil

file_list = [] #defined empty list to store text files that were moved

filexPattern = re.compile(r'\.txt$') # Regex to find text files with extension .txt

for folderName, subfolders, filenames in \
    os.walk('C:\Python Files\Automating The Boring Stuff With Python\Chapter 9 - Organizing Files\Practice Projects - Organizing Files\selective_copy_folder_1'):
    print('The current folder is '+ folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        #print('FILE INSIDE ' + folderName + ': '+ filename)
        mo = filexPattern.search(filename)
        #print(mo.group())

        if mo.group() == '.txt':
            fullPath = folderName + '\\' + filename
            #print(fullPath)
            file_list = file_list + [filename]
            shutil.copy(fullPath, 'C:\Python Files\Automating The Boring Stuff With Python\Chapter 9 - Organizing Files\Practice Projects - Organizing Files\selective_copy_to_folder')

print('Files moved are:')

for filename in file_list: # Loop through list
    print(' ' + filename)

    print('')

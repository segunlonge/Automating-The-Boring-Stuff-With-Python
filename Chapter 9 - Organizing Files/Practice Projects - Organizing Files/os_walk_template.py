import os

for folderName, subfolders, filenames in os.walk('C:\\Python Files\\Automating The Boring Stuff With Python\\Chapter 9 - Organizing Files\\Practice Projects - Organizing Files\\filling_in_the_gaps'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')


'''
Write a program that walks through a folder tree and searches for exceptionally large files
or folders- say, ones that have a file size of more than 100MB. (Remember, to get
a file's size, you can use os.path.getsize() from the os module.)

Print these files with their absolute path to the screen
'''

import os, shutil

FilePathList = []
FileDetailsList = []
destination_folder_path = 'C:\Python Files\Automating The Boring Stuff With Python\Chapter 9 - Organizing Files\Practice Projects - Organizing Files\delete_unneeded_files'

for folderName, subfolders, filenames in os.walk(destination_folder_path):
    #print('The current folder is ' + folderName)

    for filename in filenames:
        #print('Complete File Path is: ' + folderName + '\\' +  filename)
        FullPath = folderName + '\\' +  filename
        FilePathList.append(FullPath)
        FileSize = os.path.getsize(FullPath) #Get the file size in bytes of each file
        if FileSize > 1000:
            #print('Filename: ' + filename + '  ' + 'Filesize: ' + str(FileSize))
            FileDetails = 'Filename: ' + filename + '  ' + 'Filesize: ' + str(FileSize)
            FileDetailsList.append(FileDetails)

for name in FileDetailsList:
    print(name)

for path in FilePathList:
    print(path)

    #print('')
        
        
        



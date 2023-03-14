#!/usr/bin/env python3

"""Walk through a folder tree and copy all files of a particular extension."""

import os
import shutil

'''The expression with input assiging the file path to a variable does not work hence commented out'''

#folder = input('C:\\Python Files\\Automating The Boring Stuff With Python\\Chapter 9 - Organizing Files\\Practice Projects - Organizing Files\\selective_copy_folder_1')
folder = 'C:\\Python Files\\Automating The Boring Stuff With Python\\Chapter 9 - Organizing Files\\Practice Projects - Organizing Files\\selective_copy_folder_1'

#extension = input("txt")
extension = "txt"

#destination = input('C:\\Python Files\\Automating The Boring Stuff With Python\\Chapter 9 - Organizing Files\\Practice Projects - Organizing Files\\selective_copy_to_folder')
destination = 'C:\\Python Files\\Automating The Boring Stuff With Python\\Chapter 9 - Organizing Files\\Practice Projects - Organizing Files\\selective_copy_to_folder'

for folders, subfolders, filenames in os.walk(folder):

        for filename in filenames:

            if filename.endswith('{}'.format(extension)):
                shutil.copy(os.path.join(folders, filename), destination)

print('Selective copying has finished - all files of', extension,
      'type have been copied from', os.path.basename(folder), 'to',
      os.path.basename(destination))

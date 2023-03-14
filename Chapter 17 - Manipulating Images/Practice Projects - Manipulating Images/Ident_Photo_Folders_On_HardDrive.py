'''I have a bad habit of transferring files from my digital camera to temporary folders somewhere on the hard drive and then forgetting about these folders.
It would be nice to write a program that could scan the entire hard drive and find these leftover “photo folders.”
Write a program that goes through every folder on your hard drive and finds potential photo folders. Of course, first you’ll have to define what you consider a “photo folder” to be;
let’s say that it’s any folder where more than half of the files are photos.

And how do you define what files are photos? First, a photo file must have the file extension .png or .jpg.
Also, photos are large images; a photo file’s width and height must both be larger than 500 pixels.
This is a safe bet, since most digital camera photos are several thousand pixels in width and height.
As a hint, here’s a rough skeleton of what this program might look like:'''

'''
The Shebang line tells your computer that you want Python to execute this program;
the line is needed to run them from the command line
'''


#! python3  

import os
from PIL import Image

os.chdir('C:\\testpic')
extf = ['$Recycle.Bin','Program Files']

for foldername, subfolders, filenames in os.walk('C:\\testpic'):
    subfolders[:] = [d for d in subfolders if d not in extf]

    photoList = []

    numPhotoFiles = 0
    numNonPhotoFiles = 0
    
    for filename in filenames:
            
            # Open image file using Pillow.
        if (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')):
            #print(foldername)
            #print(subfolders)
            #print(filename)
            try:
                Harddrive_Image = Image.open(foldername+"\\"+filename)
                width, height = Harddrive_Image.size
                #print(width)
                #print(height)
                if width >= 500 and height >= 500:
                    numPhotoFiles += 1
                else:
                    numNonPhotoFiles += 1
                    #print(numPhotoFiles)
            except Exception:
                pass
        else:
            numNonPhotoFiles += 1
            

    total_files = numPhotoFiles + numNonPhotoFiles
    minimum_photos_requried = total_files/2
    if numPhotoFiles > minimum_photos_requried:
        print("Photo Folder:", foldername)
        
    print("photos:",numPhotoFiles)
    print("non photos:",numNonPhotoFiles)
    photoList.append(numPhotoFiles)






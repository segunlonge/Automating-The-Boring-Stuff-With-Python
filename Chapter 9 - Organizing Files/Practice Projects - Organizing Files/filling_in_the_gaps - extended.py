'''
Write a program that finds all files with a given prefix, such as spam001.txt,
spam002.txt, and so on, in a single folder and locates any gaps in the numbering
(such as if there is a spam001.txt and spam003.txt but no spam002.txt).

Have the program rename all the later files to close this gap.

As an added challenge, write another program that can insert gaps in numbered
files so that a new file can be added.
'''

import os, shutil, sys, random

#This is the counter used to match with the sequence of the txt files
FileSeqCounter = 1
InSeqIndicator = 0
FileList = []
FileReNum = 5
Counter1 = 0

#Assigned variable folder where the .txt files are kept
spamFolder = 'C:\\Python Files\\Automating The Boring Stuff With Python\\Chapter 9 - Organizing Files\\Practice Projects - Organizing Files\\filling_in_the_gaps'
withGapsFolder = 'C:\\Python Files\\Automating The Boring Stuff With Python\\Chapter 9 - Organizing Files\\Practice Projects - Organizing Files\\filling_in_the_gaps\\with_gaps'

#Walk through the directory tree to touch every file in folders and sub folders using the os.walk() function
for folderName, subfolders, filenames in os.walk(spamFolder):

    for filename in filenames:
        #print(filename)
        
        #Use lstrip to removing leading zeros from the left e.g. '00000010'.lstrip('0') = '10'
        fileseqnum = filename.rstrip('.txt') #remove .txt extension from file name
        fileseqnum = fileseqnum.lstrip('spam') #remove spam prefix from file name
        fileseqnum = fileseqnum.lstrip('0') #remove leading zeroes from the file numbering sequence

        #print(fileseqnum)

        #print(FileSeqCounter)

        #raise an exception if the txt files contain values after spam prefix that are non-numeric
        try:
            int(fileseqnum)
        except ValueError as ve:
            print('File contains no numeric value after spam prefix. Exiting')
            sys.exit() #exit python script on exception error
        
        if int(fileseqnum) == FileSeqCounter: #compare the file sequence with the FileSeqCounter
            print('File: ' + filename + ' is in sequence')
            InSeqIndicator = InSeqIndicator + 0
            FileList.append(filename)

        elif int(fileseqnum) != FileSeqCounter: #if the FileSeqCounter does not match the numeric values in the file name in sequence
                SeqOutIndicator = SeqOutIndicator + 1
                print('File: ' + filename + ' is not in sequence')
                #newfilename = 'spam'+str(FileSeqCounter).zfill(3)+'.txt' #use zfill to pad out FileSeqCounter with 0s; max length 3
                #print(newfilename)
                #print(FileSeqCounter)
                #oldfilepath_name = os.path.join(spamFolder, filename)
                #newfilepath_name = os.path.join(spamFolder, newfilename)
                #print(oldfilepath_name)
                #shutil.move(oldfilepath_name, newfilepath_name)
                
        FileSeqCounter = FileSeqCounter + 1

print(InSeqIndicator)

if InSeqIndicator == 0:
    #print(FileList)    #print file list that is in sequence
    if len(FileList) > 1:
        for i in range(3, len(FileList)):   #with this for loop a 'cut' is taken from item 3 and then
                                            #4 onwards are renamed plus one going forwards
            
            #print(FileList[i])
            FileList[i] = 'spam'+str(FileReNum).zfill(3)+'.txt'
            FileReNum = FileReNum + 1

    print(FileList)

else:
    print("Some files were out sequence, no need to insert gaps")

#print(len(FileList))

for folderName, subfolders, filenames in os.walk(spamFolder):
    for filename in filenames:

        if Counter1 == 8:
            sys.exit()
            
        #print(filename)
        #print(FileList[Counter1])
        shutil.move(os.path.join(spamFolder, filename), os.path.join(spamFolder, FileList[Counter1]))

        Counter1 = Counter1 + 1

        print(Counter1)
            

print(Counter1)
            


    

        

    

        
        

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
SeqOutIndicator = 0
FileList = []
FileReNum = 5
Counter1 = 0

#Assigned variable folder where the .txt files are kept
spamFolder = 'C:\\Python Files\\Automating The Boring Stuff With Python\\Chapter 9 - Organizing Files\\Practice Projects - Organizing Files\\filling_in_the_gaps'

'''
Walk through the directory tree to touch every file in folders and sub folders using the os.walk() feature
'''
for folderName, subfolders, filenames in os.walk(spamFolder):

    for filename in filenames:
        #print(filename)
        
        #Use lstrip to removing leading zeros from the left e.g. '00000010'.lstrip('0') = '10'
        fileseqnum = filename.rstrip('.txt') #remove .txt extension from file name
        fileseqnum = fileseqnum.lstrip('spam') #remove spam prefix from file name
        fileseqnum = fileseqnum.lstrip('0') #remove leading zeroes from the file numbering sequence

        #raise an exception if the txt files contain values after spam prefix that are non-numeric
        try:
            int(fileseqnum)
        except ValueError as ve:
            print('File contains no numeric value after spam prefix. Exiting')
            sys.exit() #exit python script on exception error
        
        if int(fileseqnum) == FileSeqCounter: #compare the file sequence with the FileSeqCounter to check for in-sequence of files
            print('File: ' + filename + ' is in sequence')
            InSeqIndicator = InSeqIndicator + 0 #InSequenceIndicator = 0 means all files are in sequence
            FileList.append(filename)

        elif int(fileseqnum) != FileSeqCounter: #if the FileSeqCounter does not match the numeric values in the file name in sequence
                SeqOutIndicator = SeqOutIndicator + 1 #...then the value of the SeqOutIndicator != 0
                print('File: ' + filename + ' is not in sequence')

        FileSeqCounter = FileSeqCounter + 1

#print(SeqOutIndicator)

'''
From the list of files generated into the FileList list cut the list in the middle and effectively insert a gap
always from item number 4
'''

if InSeqIndicator == 0:
    #print(FileList)    #print file list that is in sequence
    if len(FileList) > 1:
        for i in range(3, len(FileList)):   #with this for loop a 'cut' is taken from item 4 and then
                                            #5 onwards are renamed plus one going forwards
            
            #print(FileList[i])
            FileList[i] = 'spam'+str(FileReNum).zfill(3)+'.txt'
            FileReNum = FileReNum + 1


'''
If the file SeqOutIndicator is not 0 i.e. some files where out of sequence then exit the loop i.e. no need to insert gaps.
However, if the SeqOutIndcator is 0 i.e. all files are in sequence then use the FileList generated above (out of sequence to start renaming
the files). Stop when the counter reaches the number of elements in the new FileList
'''
if SeqOutIndicator != 0:
    print("Some files were out of sequence, no need to insert gaps")
    sys.exit()

for folderName, subfolders, filenames in os.walk(spamFolder):
    for filename in filenames:
 
        if Counter1 == len(FileList):
            sys.exit()

        print(filename+FileList[Counter1])
              
        if filename == FileList[Counter1]:
            Counter1 = Counter1 + 1
        else:
            #print(filename)
            #print(FileList[Counter1])
            shutil.move(os.path.join(spamFolder, filename), os.path.join(spamFolder, 'x'+FileList[Counter1]))
            Counter1 = Counter1 + 1


'''
Since the files can't be renamed in to a filename already present in the directory during the os.walk loop above.
I append an 'x' in front of the new name in the renaming code segment as above and then have another os.walk loop
remove the x appendage
'''
print(SeqOutIndicator)

if SeqOutIndicator == 0:
    for folderName, subfolders, filenames in os.walk(spamFolder):

        for filename in filenames:
            properfilename = filename.lstrip('x')
            shutil.move(os.path.join(spamFolder, filename), os.path.join(spamFolder, properfilename))
            

        
            


    

        

    

        
        

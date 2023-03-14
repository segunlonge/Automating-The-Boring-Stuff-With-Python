"""
Write a program to read in the contents of several text files (you can make the
text files yourself) and insert those contents into a spreadsheet, with one line of text per row. The lines of the first text
will be in the cells of column A, the lines of the second text file will be in the cells of column B, and so on.

Use the readlines() File object method to return a list of strings, one string per line in the file. For the first file, output
the first line to column 1, row 1. The second line should be written to column 1, row 2, and so on.
"""

# The shebang line tells the computer to execute code using Python
#! python3

import os, openpyxl
os.chdir('C:\\Python Files\\Automating The Boring Stuff With Python\\Chapter 12 - \
Working with Excel Spreadsheets\\Practice Projects - Working with Excel Spreadsheets')

TextFileList = []
FileNames = []

for filename in os.listdir():
    if filename.endswith('txt'):
        if filename.startswith('text_file'):
            FileNames.append(filename.rstrip('.txt')) #use rstrip to strip on the right only
            #print(filename) /check only text files begining with 'text_file' are being read
            TextFile = open(filename)
            TextFileList.append(TextFile.readlines())
            #print(TextFileList)

#print(FileNames)

#open a new work book
wb = openpyxl.Workbook()
#set the first sheet as the working sheet
desired_sheet = wb.worksheets[0]

#row and column counters for writing each column header
r = 1
c = 1

#Insert the header of each text file in each consecutive column in the first row in Excel
for j in range(len(FileNames)):
    desired_sheet.cell(row=r, column=c).value = FileNames[j]
    c = c + 1

##start at column 1
c = 1

#Loop used to populate each column with text values from each text file i.e. one sentence per row in each column
for filetext in TextFileList:
    filetextstr = ''.join(filetext) #join the list of text per text file into a string with a space inbetween each list item per text file
    #print(filetextstr)
    seperate_lines = filetextstr.split('\n') #use the split function to split the paragraph into individual lines
    r = 2 #start at row 2
    # for each textfile populate each cell in the column with sentence
    for i in range(len(seperate_lines)):
        #print(seperate_lines[i])
        desired_sheet.cell(row=r, column=c).value = seperate_lines[i]
        r = r + 1 
    #print('\n')
    c = c + 1

#Save the workbook object called wb_copy
wb.save("Text_Files_to_Spreadsheet.xlsx")

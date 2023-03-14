"""
Create a program that takes a number N from the command line and creates an
NxN multiplication  table in an Excel spreadsheet
"""

import sys, openpyxl, os
r = 1
c = 1

#Set the Current Working Directory
os.chdir('C:\\Python Files\\Automating The Boring Stuff With Python\\Chapter 12 - Working with Excel Spreadsheets\\Practice Projects - Working with Excel Spreadsheets')

#Check to see if the first command line argument has been entered if not exit
if len(sys.argv) < 2:
    print('Please enter the N number')
    sys.exit()
else:
    n_number = int(sys.argv[1])

#print(n_number)

#Call the openpyxl.Workbook() function to create a new blank workbook
wb = openpyxl.Workbook()
sheet = wb.active

for r in range(r, n_number + 1):
    c = 1
    for c in range(c, n_number + 1):
        mycell = sheet.cell(row=r, column=c)
        mycell.value = r * c 

##sheet['A1'] = n_number
wb.save('multiplication_table.xlsx')

##print(wb.sheetnames)
print(sheet)



    

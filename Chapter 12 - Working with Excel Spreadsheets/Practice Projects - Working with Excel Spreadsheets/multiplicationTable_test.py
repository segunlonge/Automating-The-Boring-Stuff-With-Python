import sys, openpyxl, os
r = 1
c = 1

n_number = 6

#Set the Current Working Directory
os.chdir('C:\\Python Files\\Automating The Boring Stuff With Python\\Chapter 12 - Working with Excel Spreadsheets\\Practice Projects - Working with Excel Spreadsheets')


#Call the openpyxl.Workbook() function to create a new blank workbook
wb = openpyxl.Workbook()
sheet = wb.active

for r in range(r, n_number):
    for c in range(c, n_number):
        mycell = sheet.cell(row=r, column=c)
##        mycell = r * c
        mycell = 'A'
        

##sheet['G1'] = n_number
wb.save('multiplication_table.xlsx')


import os, openpyxl, csv

os.chdir('C:\\Python Files\\Automating The Boring Stuff With Python\\Chapter 14 - Working with CSV Files and JSON Data\\Practice Projects - Working with CSV Files and JSON Data\\excelSpreadsheets')

for excelFile in os.listdir('.'):
    # Skip non-xlsx files, load the workbook object.
    if not excelFile.endswith('.xlsx'):
        continue
    wb = openpyxl.load_workbook(excelFile)
    for sheetName in wb.sheetnames:
        # Loop through every sheet in the workbook.
        sheet = wb[sheetName]
        csvFilename = excelFile[:-5]+'_'+sheet.title+'.csv'

        # Create the CSV filename from the Excel filename and sheet title.
        outputCSV = open(csvFilename, 'w', newline='')
        

# Create the csv.writer object for this CSV file.
        outputCSVwriter = csv.writer(outputCSV)

        # Loop through every row in the sheet.
        for row in sheet.rows:
            rowData = []    # append each cell to this list
            # Loop through each cell in the row.
            for col in row:
                # Append each cell's data to rowData.
                #print(col.value)
                rowData.append(col.value)

            # Write the rowData list to the CSV file.
            outputCSVwriter.writerow(rowData)

        outputCSV.close()
 

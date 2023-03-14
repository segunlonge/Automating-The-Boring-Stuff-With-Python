'''
Using the os.walk() function from Chapter 9, write a script that will go
through every PDF in a folder (and its subfolders) and encrypt the PDFs
using a password provided on the command line. Save each encrypted
PDF with an _encrypted.pdf suffix added to the original filename. Before
deleting the original file, have the program attempt to read and decrypt
the file to ensure that it was encrypted correctly.

Then, write a program that finds all encrypted PDFs in a folder (and its
subfolders) and creates a decrypted copy of the PDF using a provided
password. If the password is incorrect, the program should print a message
to the user and continue to the next PDF.
''' 

import os, sys
from PyPDF2 import PdfReader, PdfWriter
#os.getcwd()
os.chdir("C:\Python Files\Automating The Boring Stuff With Python\Chapter 13 - Working with PDF and word Documents\Practice Projects - Working with PDF and Word Documents\PDF files")
##os.getcwd()
path = os.getcwd()
##path

##for currentpath, dir, files in os.walk(path):
##print(files)

#A function for the second part of the exercise
def decrypt_encrypted():
    for currentpath, dirs, files in os.walk(path):
        for file in files:
            currentfile = os.path.join(currentpath,file)
            print(currentfile)
            reader = PdfReader(currentfile)
            writer = PdfWriter()

            try:
                if reader.is_encrypted:
                    reader.decrypt(password)

                currentdecryptfilepath = currentfile[:-14]+"_decrypted.pdf" #remove the ".pdf" appendix with [:-4]

                for page in reader.pages:
                    writer.add_page(page)

                with open(currentdecryptfilepath, "wb") as f:
                    writer.write(f)

                os.remove(currentfile)

            except:
                print("PDF: "+currentfile+" failed decryption")
                continue #continue to next file if there was an error in the decryting process

#Check to see if all the command line arguments have been entered. If not exit
if len(sys.argv) < 2:
    print('Please enter all arguments')
    sys.exit()
else:
    print("Number of arguments:", len(sys.argv), "arguments")
    password = sys.argv[1]
    #print(password)
    #print(type(password))

for currentpath, dirs, files in os.walk(path):
    for file in files:
        currentfile = os.path.join(currentpath,file) #os.path.join creates a OS dependent path of folder and file
        #print(currentfile)
        #Create the pdf object by opening the pdf
        reader = PdfReader(currentfile)
        #create a pdf writer object to re-write the pdf
        writer = PdfWriter()

        # Add all pages to the writer
        for page in reader.pages:
            writer.add_page(page)

        # Add a password to the new PDF to encrypt
        writer.encrypt(password)
        currentencryptfilepath = currentfile[:-4]+"_encrypted.pdf" #remove the ".pdf" appendix with [:-4]
        # Save the new PDF to a file
        with open(currentencryptfilepath, "wb") as f:
            writer.write(f)

        # Location of newly encrypted pdf
        reader = PdfReader(currentencryptfilepath)

        #read and check encrypted file and delete unencrypted original file
        if reader.is_encrypted:
            if reader.decrypt(password):
                os.remove(currentfile)

#Python function call to go through everyfolder, subfolder to get every file
decrypt_encrypted()

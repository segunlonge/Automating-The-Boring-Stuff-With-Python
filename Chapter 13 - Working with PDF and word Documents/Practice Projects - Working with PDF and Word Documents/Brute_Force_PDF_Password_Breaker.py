'''
Say you have an encrypted PDF that you have forgotten the password to, but you remember it was a single English word.
Trying to guess your forgotten password is quite a boring task.
Instead you can write a program that will decrypt the PDF by trying every possible English word until it finds one that works.
This is called a brute-force password attack. Download the text file dictionary.txt from http://nostarch.com/
automatestuff/. This dictionary file contains over 44,000 English words with one word per line.


Using the file-reading skills you learned in Chapter 8, create a list of word strings by reading this file.
Then loop over each word in this list, passing it to the decrypt() method. If this method returns the integer 0, the password was wrong and your program should
continue to the next password. If decrypt() returns 1, then your program should break out of the loop and print the hacked password.
You should try both the uppercase and lower-case form of each word.
(On my laptop, going through all 88,000 uppercase and lowercase words from the dictionary file takes a couple of minutes.
This is why you shouldn’t use a simple English word for your passwords.)
'''

import os
from PyPDF2 import PdfReader, PdfWriter

os.chdir('C:\\Python Files\\Automating The Boring Stuff With Python\\Chapter 13 - Working with PDF and word Documents\\Practice Projects - Working with PDF and Word Documents')

path = os.getcwd()
dictionary_filename = 'dictionary.txt'
pdf_filename = 'PDF_Password_Breaker_Encrypted_Copy.pdf'
trypassword = "Password not found"
reader = PdfReader(pdf_filename)
writer = PdfWriter()

with open(path+'\\'+dictionary_filename) as dictionaryfile:
    for line in dictionaryfile:
        trypassword = line.strip() #trypassword.lower() trypassword.upper()
        if reader.is_encrypted:
            trypassword = trypassword.lower()
            #print(trypassword)
            ispasswordcorrect = reader.decrypt(trypassword)
            #print(ispasswordcorrect)
            if str(ispasswordcorrect) == "PasswordType.OWNER_PASSWORD":
                break

        if reader.is_encrypted:
            trypassword = trypassword.upper()
            #print(trypassword)
            ispasswordcorrect = reader.decrypt(trypassword)
            #print(ispasswordcorrect)
            if str(ispasswordcorrect) == "PasswordType.OWNER_PASSWORD":
                break

print(trypassword)



        
        
    

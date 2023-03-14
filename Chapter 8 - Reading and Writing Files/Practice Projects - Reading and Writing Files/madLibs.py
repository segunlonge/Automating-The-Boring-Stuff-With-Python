'''A Mad Libs program that reads in text files and lets the user add their own
text anywhere the word ADJECTIVE, NOUN, ADVERB or VERB appears in the text file'''

import os, glob
os.chdir("C:\\Python Files\\Automating The Boring Stuff With Python\\Chapter 8 - Reading and Writing Files\\Practice Projects\\madLibsTextFiles")

''' Loop through each text file in the working directory using the glob module to
to search for *.txt files'''


WordSearch = ['ADJECTIVE','NOUN','ADVERB','VERB'] #A list containing the words to search for in the text file

for textFile in glob.glob("*.txt"):
    currentFile = open(textFile) #open the text file and assign it to a file object
    print(textFile) #print the name of the text file
    textCurrentFile = currentFile.read() #read the contents of the text file and assign to a variable
    print(textCurrentFile) #print the contents of the text file
    for i in range(len(WordSearch)): #search for each consecutive index from the list in the contents of the text file
        if textCurrentFile.find(WordSearch[i]) > 0: #find returns -1 if text not found...
            WordReplace = input('Word '+WordSearch[i]+' was found. Replace with? ') #...if text found get replacement word from user
            textCurrentFile = textCurrentFile.replace(WordSearch[i],WordReplace) # replace the word found in the list with the inputted word

    print(textCurrentFile) #print newly changed contents from the variable

    currentFile.close() #close the file object

    NewFile = open(textFile+"_new.txt", 'w') #open a new file object in write mode 
    NewFile.write(textCurrentFile) #write the new contents to the file

    NewFile.close() #close the new file

    
            
        
    
    
    
    

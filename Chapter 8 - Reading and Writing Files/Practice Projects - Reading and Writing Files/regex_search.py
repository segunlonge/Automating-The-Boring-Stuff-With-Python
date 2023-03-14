'''A program that opens all *.txt files in a folder and searches for any line that
matches a user-supplied regular expression. The results are printed on screen'''

import os, glob, re
os.chdir("C:\Python Files\Automating The Boring Stuff With Python\Chapter 8 - \
Reading and Writing Files\Practice Projects - Reading and Writing Files\RegexSearchTextFiles")
# Note \ means line continuation i.e. to break up a long line

userRegex = re.compile(input('Enter your Regex expression :'))

for textFile in glob.glob("*.txt"):
    currentFile = open(textFile) #open the text file and assign it to a file object
    textCurrentFile = currentFile.read() #read the contents of the text file and assign to a variable
    print(textCurrentFile)
    #print(type(textCurrentFile))
    searchedText = userRegex.search(textCurrentFile)
    #print("Found Regex matches: ", searchedText.group() if searchedText else None) Alternative to the If...Then...else structure

    if searchedText == None:
        print("No match for inputted Regex expression")
    else:
        print("Found Regex matches: ", searchedText.group())

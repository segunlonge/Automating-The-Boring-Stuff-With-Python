'''
Write a function that takes a string and does the same thing as the strip()
string method. If no arguments are passed other than the string to strip, then
whitespace characters will be removed from the beginning and end of the string.
Otherwise characters specified in second argumnent to the function will be
removed from the string
'''

import re

inputstring = input()
findall_list = []

def CustomStrip(inputstring, pattern=" "): #set pattern default argument to space
    stripRegex = re.compile(pattern) #create regex object for the pattern to match
    findall_list = stripRegex.findall(inputstring) #use findall to find the pattern in the input string
    print(stripRegex.findall(inputstring))
    print(len(findall_list))

    if len(findall_list) > 0:
        stripped_string = inputstring.replace(pattern,"")
        print(stripped_string)
    else:
        print(inputstring)

CustomStrip(inputstring)
    

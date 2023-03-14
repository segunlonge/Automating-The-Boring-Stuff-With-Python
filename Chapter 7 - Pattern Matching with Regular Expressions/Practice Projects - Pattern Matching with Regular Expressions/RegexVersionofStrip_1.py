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
    stripRegexbeg = re.compile('^'+pattern+'*') #create regex object for the pattern to match
    stripRegexend = re.compile(pattern+'$') #create regex object for the pattern to match
    print(stripRegexbeg)
    #print(stripRegexend)
    search_beg = stripRegexbeg.search(inputstring) == None
    print(search_beg)
    search_end = stripRegexbeg.search(inputstring) == None
    print(search_end)

    if search_beg == False:
        stripped_string_beg = inputstring.replace(pattern,"")
        print(stripped_string_beg)

##    if search_end == False:
##        stripped_string_end = inputstring.replace(pattern,"",len(stripped_string_beg)-1)
##        print(stripped_string_end)
        
    #stripRegexend.search(inputstring) 
##    print(len(searched_beg))

##    if len(searched_beg) > 0:
##        stripped_string = inputstring.replace(pattern,"")
##        print(stripped_string)
##    else:
##        print(inputstring)

CustomStrip(inputstring)


'''
restart: use this: reg1 = re.compile(r'\w+') / reg1.findall(inputstring)
    

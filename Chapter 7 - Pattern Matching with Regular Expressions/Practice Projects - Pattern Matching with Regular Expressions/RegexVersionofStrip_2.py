'''
Write a function that takes a string and does the same thing as the strip()
string method. If no arguments are passed other than the string to strip, then
whitespace characters will be removed from the beginning and end of the string.
Otherwise characters specified in second argumnent to the function will be
removed from the string
'''

import re

# A right-replace function found online
def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

inputstring = input()
findall_list = []

def CustomStrip(inputstring, pattern=" "): #set pattern default argument to space
    stripRegexbeg = re.compile('^'+pattern+'*') #create regex object for the pattern to match
    stripRegexend = re.compile(pattern+'$') #create regex object for the pattern to match
    #print(stripRegexbeg)
    #print(stripRegexend)
    search_beg = stripRegexbeg.search(inputstring) == None
    print(search_beg)
    span_1 = stripRegexbeg.search(inputstring)
    search_beg_number = span_1.span()
    print(search_beg_number[1])
    
    search_end = stripRegexend.search(inputstring) == None
    print(search_end)
    span_2 = stripRegexbeg.search(inputstring)
    search_end_number = span_2.span()
    print(search_end_number[1])
    

    if search_beg == False:
        stripped_string_beg = inputstring.replace(pattern,"",search_beg_number[1])
        #print(stripped_string_beg)

    if search_end == False:
        #stripped_string_end = inputstring.replace(pattern,"",len(stripped_string_beg)-search_end_number[1])
        stripped_string_end = rreplace(stripped_string_beg,pattern,'',search_end_number[1])
        print(stripped_string_end)
        
CustomStrip(inputstring, "-")

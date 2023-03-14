"""Write a function that takes a string and does the same thing as the strip() method. If no other arguments are
passed other than the string to strip, then whitespace characters will be removed from the beginning and end of
the string. Otherwise, the characters specified in the second argument to the function will be removed from the string."""

"""The strip() string method removes whitespace at the beginning or end of a string"""

import re

removeWhiteSpace = re.compile(r'''(
(^\s+|\s+$) # remove white space found at the beginning or end of the string
)''', re.VERBOSE)

def whitepacestrip(argstring, argcha=""):
    if removeWhiteSpace.search(argstring) == None:
        print(argstring)
    else:
        cleanstring = removeWhiteSpace.sub(argcha,argstring)
        print(cleanstring)

whitepacestrip('    Hello World    ',"")

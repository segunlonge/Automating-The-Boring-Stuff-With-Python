#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()
#print(text)

#Separate lines and add stars
lines = text.split('\n') #split copied text into list form
#print(lines)
for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines) #Join the list back into line by line items
pyperclip.copy(text)

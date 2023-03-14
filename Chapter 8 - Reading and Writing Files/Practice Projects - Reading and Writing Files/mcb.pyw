#! python3
 # mcb.pyw - Saves and loads pieces of text to the clipboard.
 # Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
 #        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
 #        py.exe mcb.pyw list - Loads all keywords to clipbaord.
 #Notes:
 #The .pyw extension means that Python won't show a Terminal window when it...
 #...runs the program



# pyperlicp is for copying and pasting
# sys is for reading command line arguments
# shelve lets us save clippoard data to and copy from an .mcb file
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Check to see if there are 2 arguments and the first one contains the word "save"
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    # If so take the second argument and use as keyword for the dictionary. Paste the value of the clipboard to the...
    # ...key value pair.
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    # If only one argument then assume its a list or keyword to load its content onto the clipboard
elif len(sys.argv) == 2:
     # If there's only one command line argument check whether the argument is "list" and...
     # ...list of keys
    if sys.argv[1].lower() == 'list':
         pyperclip.copy(str(list(mcbShelf.keys())))
     # Else if assuming it is a keyword then it must be in the mcbShelf file so copy it to the clipboard
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

     

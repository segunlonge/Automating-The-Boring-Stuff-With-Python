#! python3
 # mcb.pyw - Saves and loads pieces of text to the clipboard.
 # Usage: py.exe mcb_extended.pyw save <keyword> - Saves clipboard to keyword.
 #        py.exe mcb_extended.pyw <keyword> - Loads keyword to clipboard.
 #        py.exe mcb_extended.pyw list - Loads all keywords to clipbaord.
 #        py.exe mcb_extended.pyw delete_all - Deletes all keywords in the shelf
 #        py.exe mcb_extended.pyw delete <keyword> - Deletes all keywords in the shelf 
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
    # If so take the second argument and use as keyword. Paste the value of the clipboard to the...
    # ...keyword value pair.
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

# deletes a key word from the shelf data file passing delete argument and key...
# ...or just the delete_all keyword which clears the who shelf file
if len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delete_all':
    mcbShelf.clear()
    print('The shelf file has been cleared')

mcbShelf.close()

     

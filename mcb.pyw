#! python3
# mcb.pyw multiclipboard script

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
   #        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
   #        py.exe mcb.pyw list - Loads all keywords to clipboard.

import pyperclip, sys, shelve

mcbShelf = shelve.open('mcb')


   # TODO: fix saving to shelve
if len(sys.argv) == 3 and sys.argv[1] == "save":
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print("Clipboard saved")
elif len(sys.argv) == 3 and sys.argv[1] == "delete":
    del mcbShelf[sys.argv[2]]
    print(sys.argv[2] + " deleted")
elif len(sys.argv) == 2:
    # List keys
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()


'''The while statement executes the block of code underneath repeatedly until it encounters the
break statement i.e. when no user input is entered
'''

catNames = [] #an empty list variable is defined at the beginning
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] #list concatenation technique
print('The cat names are:')
for name in catNames:
    print(' ' + name)

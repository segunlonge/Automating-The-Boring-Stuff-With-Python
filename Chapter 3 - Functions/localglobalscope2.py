'Example of one function (spam) calling another function (bacon)
'When the bacon function is called within the spam function the local variable
'eggs in bacon is set to 0 but eggs = 99 is returned i.e. no clash of
'the two local variables

def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
eggs = 0

spam()

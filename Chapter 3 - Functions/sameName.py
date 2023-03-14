"""The below illustrates why not to use the same name for global and local variables
python would not make a distinction between local and global variables
"""
def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'
def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints bacon local
eggs = 'global'
bacon()
print(eggs) # prints 'global'

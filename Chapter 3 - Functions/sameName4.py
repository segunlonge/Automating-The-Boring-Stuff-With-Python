"""
This illustrates that the egg variable needed to be set before the print function but that in this case
the function does not fall back on the gloably set egg variable
"""

def spam():
    #eggs = 'spam local'
    print(eggs) # ERROR!
    eggs = 'spam local'

eggs = 'global'
spam()


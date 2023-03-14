"""
Don't create a local variable with the variable name called eggs
Allows you to modify a global variable from within a function.
If the global keyword had not been used then the out put of eggs would be 'global'
"""

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)


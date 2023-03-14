'The global variable (eggs) can be read from a local scope hence why the
'value is printed twice: 1)when function is called and again when print function
'is called
def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)

'Cannot call a local variable (i.e. defined in a function) at a global level
def spam():
    eggs = 31337
spam()
print(eggs)

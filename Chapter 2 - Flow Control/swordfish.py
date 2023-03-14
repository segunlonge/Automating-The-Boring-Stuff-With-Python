while True:
    print('Who are you?')
    name = input()
    if name !='Joe':
        continue #Go back to the begining of the loop and re-evaluate
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
    print('Access granted.')

#Create the initial dictionary with storage of some birthdays
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

'''Use the while loop to keep asking for the enter name dialogue and quite
until is enter is pressed on a blank input'''
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break


    '''check if name entered is in dictionary and print birthday else
    if not then ask for birthday of new name and add name and birthday to
    dictionary'''
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()

        birthdays[name] = bday
        print('Birthday database updated.')

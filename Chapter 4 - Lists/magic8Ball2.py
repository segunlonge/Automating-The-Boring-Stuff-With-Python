import random

messages = ['It is certain',
            'It is decidedly so'
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']
print(messages[random.randint(0,len(messages)-1)])

'''len = 8-1 = 7 and the random number generated should be between
0 - 7 which are 8 random numbers

Which ever random number is generated is the item in the list that is printed
'''

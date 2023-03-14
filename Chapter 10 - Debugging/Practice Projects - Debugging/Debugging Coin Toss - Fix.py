'''The following program is meant to be a simple coin toss guessing game. The
player gets two guesses (it's an easy game). However, the program has several bugs in it.
Run through the program a few times to find the bugs that keep the program from
working correctly.

The issue was the comparing the value of guess which is a string
to the value of toss which is an integer
'''

import random
guess = ''
guess_2 = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    
if guess == 'heads':
    guess_2 = 1
else:
    guess_2 = 0
    
toss = random.randint(0,1) # 0 is tails, 1 is heads
if toss == guess_2:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    
    if guess == 'heads':
        guess_2 = 1
    else:
        guess_2 = 0
    
    if toss == guess_2:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

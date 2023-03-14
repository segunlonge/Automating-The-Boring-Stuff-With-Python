"""
Write a function that uses regular expressions to make sure the password string
it is passed is strong.

A strong password is defined as one that is at least eight characters long,
contains both uppercase and lowercase characters, and has at least one digit.
You may need to test the string against multiple regex patterns to validate its
strength
"""

#import regex functions
import re

#create regex objects
AlphaNum = re.compile(r'[a-zA-Z0-9]+') #check for alpahnumeric
Digit = re.compile(r'\d+') #check for at least 1 digit
UCase = re.compile(r'[a-z]') #check for upper case
LCase = re.compile(r'[A-Z]') #check for lower case

password = input()

def PasswordCheck(password):
    if AlphaNum.search(password) and Digit.search(password) and len(password)>= 8 \
       and UCase.search(password) and LCase.search(password):
        return True
    else:
        return False

#print(PasswordCheck(password))

if PasswordCheck(password) is True:
    print('This is a strong password')
else:
    print('This password is weak')


def isPhoneNumber(text):
    if len(text) !=12: #check if string is 12 characters long
        return False
    for i in range(0, 3):
        if not text[i].isdecimal(): #check if first first 3 characters consist of only numbers
            return False
        if text[3] != '-': #check if 4th character has '-'
            return False
        for i in range(4, 7):
            if not text[i].isdecimal(): #check if middle characters are numbers
                return False
            if text[7] != '-': #check if 8th character has '-'
                return False
            for i in range(8, 12):
                if not text[i].isdecimal(): #check if last characters are numbers
                    return False
                return True

##print('415-555-4242 is a phone number:')
##print(isPhoneNumber('415-555-4242'))
##print('Moshi moshi is a phone number:')
##print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

#The for loop passes a chunck of 12 characters from message to the isPhoneNumber function
#It takes 12 chunk at a time moving 1 character to the right on each iteration
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

#! python3
# textMyself.py - Defines the testmyself() function that texts a message passed to it as a string.

# Present values:
accountSID = 'AC8e86f44fe2e1f4dd05b87bb1053c6f66'
authToken = 'd027aa0c54ff50853f62848262ddb3a9'
twilioNumber = '+14322871536'
myNumber = '+447951585752'

from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)

textmyself('ABC')
    

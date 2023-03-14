import smtplib, random
from getpass import getpass

smtpObj = smtplib.SMTP('smtp.fastmail.com', 587)
smtpObj.ehlo()

smtpObj.starttls()

#password = getpass()

smtpObj.login('slonge@xsmail.com', '4yd38ywtbhfssfu8')
print('Successfull')

EmailAddresses = ['slonge@xsmail.com', 'admin@adivardhan.tech']
chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']

for E in EmailAddresses:
    randomChore = random.choice(chores)
    smtpObj.sendmail('slonge@xsmail.com', E, 'From: slonge@xsmail.com\r\nTo: '+E+'\r\nSubject: Chore\r\n'+randomChore)
    chores.remove(randomChore) # this chore is now taken, so remove it

    print('Email sent')








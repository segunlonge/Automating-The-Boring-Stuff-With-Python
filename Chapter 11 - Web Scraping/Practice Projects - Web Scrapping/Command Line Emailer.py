'''
Write a program that takes an email address and string of text on the command line and then, using Selenium,
logs into your email account and sends an email of the string to the provided address.
(You might want to set up a separate email account for this program.)
This would be a nice way to add a notification feature to your programs.
You could also write a similar program to send messages from a Facebook or Twitter account.

To run from CMD navigate to folder of script and if spaces in name enclose in
"" marks
'''
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
options = Options()
options.add_argument("start-maximized")

#Check to see if all the command line arguments have been entered. If not exit
if len(sys.argv) < 3:
    print('Please enter all arguments after script name as: [reciever\'s email] [email body]')
    print('Argument 1: reciever\'s email')
    print('Argument 2: email body')
    sys.exit()
else:
    print("Number of arguments:", len(sys.argv), "arguments")
    email_reciever = sys.argv[1]
    body = sys.argv[2]

#Loop through entered command line arguments skipping the first one i.e. filename
for x in sys.argv[1:]:
    print(x, end=' ')

#Start a Chrome session; initiate the Chromedriver
webdriver_service = Service('C:\MyPythonScripts\chromedriver.exe')
driver = webdriver.Chrome(service=webdriver_service, options=options)

url = 'https://www.fastmail.com/login/'
#Open the url specified
driver.get(url)
#Selenium to wait a maximum of 20 seconds for an element to be loaded and found
wait = WebDriverWait(driver, 20)

#Variables
senderLogon = "slonge@xsmail.com"
senderPassword = "xxxxxxx"
emailSubject = "Selenium Browser Email Automation"

#An explicit wait code (EC...) to wait for the specified web element to load
#Also checks that the element is clickable and visible i.e. EC.element_to_be_clickable
username_field = wait.until(EC.element_to_be_clickable((By.ID, "v16-input")))
password_field = wait.until(EC.element_to_be_clickable((By.ID, "v17-input")))

#print(username_field)

#Send keys is used to send data to identified fields in the web browser
username_field.send_keys(senderLogon)
password_field.send_keys(senderPassword)

loggin_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="v10"]/div/p/button')))
loggin_button.click()

compose_button = wait.until(EC.element_to_be_clickable((By.ID, "v133")))
compose_button.click()

#to_field = wait.until(EC.element_to_be_clickable((By.ID, "v299-to-input")))
to_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".s-compose-to textarea")))
print(to_field)
to_field.send_keys(email_reciever)
##to_subject = wait.until(EC.element_to_be_clickable((By.ID, "v299-subject-input")))
to_subject = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".s-compose-subject input")))
print(to_subject)
to_subject.send_keys(emailSubject)
email_body = wait.until(EC.element_to_be_clickable((By.ID, "defanged1")))
print(email_body)
email_body.send_keys(body)
#send_button = wait.until(EC.element_to_be_clickable((By.ID, "v163")))
send_button = wait.until(EC.element_to_be_clickable((By.ID, "v151")))
send_button.click()


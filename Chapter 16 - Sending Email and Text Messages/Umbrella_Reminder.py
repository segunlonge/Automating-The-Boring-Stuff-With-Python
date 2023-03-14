'''Chapter 11 showed you how to use the requests module to scrape data from http://weather.gov/.
Write a program that runs just before you wake up in the morning and checks whether it’s raining that day.
If so, have the program text you a reminder to pack an umbrella before leaving the house.
'''

import requests
from bs4 import BeautifulSoup
from textMyself import textmyself

res = requests.get('https://www.bbc.co.uk/weather/2641290')

soup = BeautifulSoup(res.content, 'html.parser')
#print(soup)
wheather_cond = soup.find("div",{"class":"wr-day-summary"}).find("span").text
print(wheather_cond)

if 'rain' in wheather_cond:
    #send text via twilio
	textmyself("Carry Umbrella")


'''Write a program that checks the websites of several web comics and automatically downloads the
images if the comic was updated since the program’s last visit.

Your operating system’s scheduler(Scheduled Tasks on Windows, launchd on OS X, and cron on Linux)
can run your Python program once a day. The Python program itself can download the comic and then
copy it to your desktop so that it is easy to find. This will free you from having to check the website
yourself to see whether it has updated.'''

#! python3
# Scheduled Web Comic Downloader.py - Downloads comics.

import os

from bs4 import BeautifulSoup
import requests

def lunarbaboon(url, soup):
    image_url = url+soup.find_all("img")[2]['src']
    image_name = image_url.split("?")[0].split("/")[-1]
    return image_url,image_name

def nonadventures(url, soup):
    output = soup.find("div",{"id":"comic"})
    image_url = output.find("img")['src']
    image_name = image_url.split("/")[-1]
    return image_url,image_name

def savagechickens(url, soup):
    output = soup.find("div",{"class":"entry_content"})
    image_url = output.find("img")['src']
    image_name = image_url.split("/")[-1]
    return image_url,image_name


# The relevant URL
urls = ["http://www.lunarbaboon.com", "http://www.nonadventures.com", "https://www.savagechickens.com"]
for url in urls:
    website_name = url.split(".")[1]
    os.chdir('C:\\Python Files\\Automating The Boring Stuff With Python\\Chapter 15 - Keeping Time, Scheduling Tasks, and Launching Programs\\'+website_name)

    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    image_url,image_name = eval(website_name)(url, soup)
    if not os.path.isfile(image_name):
        image_data = requests.get(image_url).content
        #print(image)

        with open(image_name, 'wb') as f:
            f.write(image_data)
    else:
        print("image already exists")
        





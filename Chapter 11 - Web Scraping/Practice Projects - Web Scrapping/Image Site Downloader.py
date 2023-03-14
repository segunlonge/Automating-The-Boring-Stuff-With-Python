'''
Write a program that goes to a photo-sharing site like flickr or Imgur, searches for a category of photos, and then downloads all the
resulting images. You could write a program that works with any photo site that has a search feature.
'''

import os

from bs4 import BeautifulSoup #Beautiful Soup is a Python package for parsing HTML and XML documents
import requests #Used for requesting a webpage

#Set the working directory
os.chdir('C:\\Python Files\\Automating The Boring Stuff With Python\\Chapter 11 - Web Scraping\\Practice Projects - Web Scrapping\\ImageSiteDownloader')

#The relevant URL 
url = "https://www.flickr.com/search/?text=chihuahua"

#The option 'html.parser' parses the contents of the webpage as an html page in text
soup = BeautifulSoup(requests.get(url).content, 'html.parser')
#list of tags in the form of a dictionary
images = soup.find_all("img")
#print(images)
#print(images[0]['src']) #Example print link of image i.e. location of image url

#loop through all the text for images url parsed
for i in range(len(images)):
    if "https:" not in images[i]['src']: #if url does not contain https
        img_data = requests.get("https:"+images[i]['src']).content #Actual image is the content of src
    else:
        img_data = requests.get(images[i]['src']).content #Actual image is the content of src
    image_name = images[i]['src'].split("/")[-1] #split by "/" and return the last item in the list i.e. the image name
    print(image_name)
    #with open(image_name, 'wb') as f:
    #    f.write(img_data)

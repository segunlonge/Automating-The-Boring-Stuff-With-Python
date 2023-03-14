'''
Write a program that, given the URL of a web page, will attempt to download every
linked page on the webpage. The program should flag any pages that have a 404 "Not Found"
status code and print them out as broken links.

Example link: https://www.mathsisfun.com/links/external.html
'''

import requests, bs4, os, sys

#change working directory
os.chdir('C:\\Python Files\\Automating The Boring Stuff With Python\\Chapter 11 - Web Scraping\\Practice Projects - Web Scrapping')

#input prompt to enter URL
url = input("Please enter a URL: ")

#list to capture broken links
broken_weblink_list = []

#
res = requests.get(url)
#print(res.raise_for_status())
#parse the html of the website as text
urlSoup = bs4.BeautifulSoup(res.text, 'html.parser')

#print(urlSoup)

with open('web_links.txt', 'w', encoding='utf-8') as f:
    for link in urlSoup.find_all('a'):
        try:
            res.raise_for_status()
        except:
            print(link.get('href')+' is a broken link')
            broken_weblink_list = link.get('href')
            
        #print(link.get('href'))
        f.write(str(link.get('href'))+'\n')

for l in broken_weblink_list:
    broken_weblink_list = link.get('href')
    f.write(str(l)+': is a broken link'+'\n')

sys.exit()




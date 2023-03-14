#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
# soup = bs4.BeautifulSoup(res.text)
soup = bs4.BeautifulSoup(res.text, 'html.parser') 
#print(soup)

# Open a browser tab for each result
linkElems = soup.select(' .LC201b DKV0Md a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

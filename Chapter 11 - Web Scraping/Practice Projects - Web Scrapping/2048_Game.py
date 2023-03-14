'''
2048 is a simple game where you combine tiles by sliding them up, down, left, or right
with the arrow keys. You can actually get a fairly high score by repeatedly sliding in an up,
right, down, and left pattern over and over again.

Write a program that will open the game and keep sending up, right, down, and left keystrokes to automatically
play the game

https://play2048.co/
'''

print("Done")

import re

gameEndRegex = re.compile(r'^Game over!')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("start-maximized")

#Start a Chrome session; initiate the Chromedriver
webdriver_service = Service('C:\Python Files\Automating The Boring Stuff With Python\Chapter 11 - Web Scraping\Practice Projects - Web Scrapping\chromedriver.exe')
driver = webdriver.Chrome(service=webdriver_service, options=options)

url = 'https://play2048.co/'
driver.get(url)
wait = WebDriverWait(driver, 1)

cookie_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/p/span/button[2]')))
cookie_button.click()

game = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "body")))

GameOver = None

while True:
    try: #capture error arising out of the end game message not being present until game has ended
        GameOver = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.game-message.game-over'))).text
        #visibility_of_element_located
        #presence_of_element_located
    except:
        game.send_keys(Keys.ARROW_UP)
        game.send_keys(Keys.ARROW_RIGHT)
        game.send_keys(Keys.ARROW_DOWN)
        game.send_keys(Keys.ARROW_LEFT)

    if GameOver != None:
        break

#print("Done")
print(GameOver)

if gameEndRegex.search(GameOver) != None:
    print("Finished")
















import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Selenium Webdriver
s = Service("chromedriver.exe")
driver = webdriver.Chrome(service = s)


page_url = "https://leetcode.com/problemset/all/?page="


def get_all_links(url):
    driver.get(url)
    time.sleep(7)

    arr = driver.find_elements(By.TAG_NAME, "a")

    links = []
    pattern = "/problems"

    for i in arr:
        try:
            href = i.get_attribute('href')
            if(pattern in href):
                links.append(href)
        except:
            pass
    
    links = list(set(links))

    return links


# Calling get links for all 55 pages
links=[]
for i in range(1,56):
    url = page_url+str(i)
    links+=get_all_links(url)

links = list(set(links))



# Now we can store these links in a txt file
# Open txt file lc.txt in a mode
with open('prob.txt', 'a')as file:
    for i in links:
        file.write(i)
        file.write('\n')

driver.quit()
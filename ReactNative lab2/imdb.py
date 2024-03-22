from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import json
import time

chrome_binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
chromedriver_path = "G:/Cods/chromeDriver/chromedriver.exe"
url = "http://www.imdb.com"

chrome_options = Options()
chrome_options.binary_location = chrome_binary_location
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

def join_content(jc):
    return ','.join(jc)

def iterate_actors(iter_actors):
    m = []
    for item in iter_actors:
        m.append(item['name'])
    return ','.join(m)

def prepare_content(json_content):
    d = {}
    d['image'] = json_content['image']
    d['name'] = json_content['name']
    d['url_content'] = url + json_content['url']
    d['genre'] = join_content(json_content['genre'])
    d['actors'] = iterate_actors(json_content['actor'])
    d['description'] = json_content['description']
    d['trailer'] = url + json_content['trailer']['embedUrl']
    return d

def imdb_searchbox(url, link):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    wait = WebDriverWait(driver, 20)  # Increase timeout to 20 seconds
    try:
        searchbox = wait.until(EC.presence_of_element_located((By.ID, "suggestion-search")))
    except TimeoutException as e:
        print("Timeout occurred:", e)
        driver.quit()
        return None
    
    searchbox.click()
    searchbox.send_keys(link)
    time.sleep(1)
    driver.find_element(By.ID, "react-autowhatever-navSuggestionSearch--item-0").click()
    json_content = json.loads(driver.find_element(By.CSS_SELECTOR, 'script[type="application/ld+json"]').get_attribute("innerText"))
    driver.quit()
    return prepare_content(json_content)

def imdb_search(link):
    s = imdb_searchbox(url, link)
    return s

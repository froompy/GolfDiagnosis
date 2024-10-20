from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import re
import requests

# service = webdriver.ChromeService(executable_path=r'C:\Users\froom\.cache\selenium\chromedriver\chromedriver.exe')
# driver = webdriver.Chrome(service=service)
options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)
driver.minimize_window() # For maximizing window

# driver.implicitly_wait(3) # gives an implicit wait for 20 seconds      

url = r'C:\Users\froom\OneDrive\Documents\Docs\Coding\Python\Web Scrape\Garmin scrape/source.html'
# url = r'https://connect.garmin.com/modern/scorecards/03791680-38d1-4195-99f4-b8123983288a'
driver.get(url)


# course = driver.find_elements(By.XPATH, """/html/body/section[2]/div/div/div/div/table/tbody/tr""")
# course = driver.find_element(By.XPATH, """//*[@id="pageContainer"]/div[2]/div/div/div[2]/div[2]/a""")

# ddd = driver.find_elements(By.CLASS_NAME,'truncate')
# ddd = driver.find_element(By.TAG_NAME,("//*[contains(text(),'modern')]"))
# fff = driver.find_element(By.XPATH,"""//*[@id="pageContainer"]/div[2]/div/div/div[14]/div[2]/a""")
# fff = driver.find_element(By.XPATH,'/html/body/div/div[6]/div[2]/a')
# fff = driver.find_elements(By.XPATH,value="/html/body/div/div[6]/div[2]/a")

pp = driver.find_elements(By.CLASS_NAME,value=f"""GolfList_listItem__0fxyw""")
count_rounds = (len(pp))
numb_success = 1
numb_fail = 1

rounds_played = []
for i in range(2,count_rounds):
    try:
        if driver.find_element(By.CLASS_NAME,f"""GolfList_listItem__0fxyw"""):
            fff = driver.find_element(By.XPATH,value=f"""/html/body/div/div[{i}]/div[2]/a""")
            uu = fff.get_attribute('href')
            pp = re.search(r"[0-9]+",uu)
            rounds_played.append(pp.group())
            numb_success+=1
            if i == count_rounds-1:
                for j in range(i+1,i + numb_fail+2):
                    fff = driver.find_element(By.XPATH,value=f"""/html/body/div/div[{j}]/div[2]/a""")
                    uu = fff.get_attribute('href')
                    pp = re.search(r"[0-9]+",uu)
                    rounds_played.append(pp.group())
    except:
        pass
        numb_fail+=1
print(f"Number of rounds played: {len(rounds_played)}")
print(rounds_played)
########################Print off details about the round (Score, course, date)
# rrr = driver.find_elements(By.CLASS_NAME,f"""GolfList_listItem__0fxyw""")
# print(rrr[1].text)
# print(f"Success number is {numb_success}")
# print(f"Fail number is {numb_fail}")


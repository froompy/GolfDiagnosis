from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import numpy as np
import os
from pathlib import Path

service = webdriver.ChromeService(executable_path=r'C:\Users\froom\.cache\selenium\chromedriver\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.minimize_window() # For maximizing window
driver.implicitly_wait(10) # gives an implicit wait for 20 seconds      

def removespace(list):
    spliced_list = []
    for i in list:
        try:
            pd.isnull(int(i))
            spliced_list.append(int(i))
        except:
            if i == """—""":
                spliced_list.append(0)
            pass
    return spliced_list

def pullscores(round):
    url = f'https://connect.garmin.com/modern/scorecard/new/{round}'
    driver.get(url)
    scores = driver.find_elements(By.CLASS_NAME,"GolfScorecardPage_holeItem__PuUpc")
    course = driver.find_element(By.XPATH, """//*[@id="pageContainer"]/div/div/div[1]/div[2]/h3""")
    coursedate = driver.find_element(By.XPATH, """//*[@id="pageContainer"]/div/div/div[1]/div[3]/div[2]/div[2]""")
    coursetype = driver.find_element(By.XPATH,"""//*[@id="pageContainer"]/div/div/div[1]/div[3]/div[2]/div[1]""")

    total_of_scorecards = []
    for score in scores:
        total_of_scorecards.append(score.text)
    total_of_scorecards = removespace(total_of_scorecards)

    total_holes =  total_of_scorecards[0:9] + total_of_scorecards[36:45]
    total_pars = total_of_scorecards[9:18] + total_of_scorecards[45:54]
    total_scores = total_of_scorecards[18:27] +  total_of_scorecards[54:63]
    total_putts = total_of_scorecards[27:36] + total_of_scorecards[63:72]
    total_stats = []
    total_stats = zip(total_holes,total_pars,total_scores,total_putts)
    df = pd.DataFrame(total_stats, columns=['Hole','Par','Strokes','Putts'])
    df['Course'] = course.text
    df['Date'] = coursedate.text
    df['Type'] = coursetype.text
    df['Round'] = round
    return(df)

dfTotal = pd.DataFrame()
round_number = [     
             '295091379', '294123266', '293201465', '293025663', '291479724', '291353013', '290916822', '290391948',
             '290207758', '289408501', '289232096', '288338715', '287222496', '286407819', '285540372', '283421691',
             '281564078', '280410326', '279446418', '278296074', '277521712', '276715541', '275627706', '275449227',
             '274705720', '259050848', '257530523', '257244569', '256632384', '254782295', '254352942', '254127125', 
             '253256711', '252893596', '252337491', '251469139', '250592824', '250171031', '249726009', '249523588', 
             '248798900', '247395788', '247025622', '246300040', '246152005', '244580845', '244208914', '244139251', 
             '242566822', '241934486', '241663052', '240862555', '225847253', '224445090', '223759084', '223644395',
             '222886586', '221462176', '220506165', '219787176', '218766901', '218765721', '217931680', '216879227', 
             '216192605', '214453845', '214298672', '212872239', '212768404', '212668548', '210374480', '207914229',
             '207044525', '206246526', '192567809', '192242439', '192063082', '191248627', '190509401', '189612589',
             '189015514', '187451694', '187046243', '186703880', '186566041', '186499953', '186491399', '185720700',
             '185517710', '185467260', '185464543', '183413339', '182416600', '182412412', '181986350', '181599144',
             '181484825', '180632190', '180478038', '180006861', '179664075', '179428006', '179288645', '179069156',
             '178430604', '177752651', '177484660', '177318045', '177112281', '176383214', '175298983', '174900062'
]

for i in round_number:
    try:
        dfTemp = pd.DataFrame(pullscores(i))
        dfTotal = pd.concat([dfTotal,dfTemp])
    except:
        print(f'Screwed up rounds:  {i}')

dfTotal.to_csv(path_or_buf=r'''C:\Users\froom\OneDrive\Documents\Docs\Coding\Python\Web Scrape\Garmin scrape\scorecards.csv''',mode='a',header=False)
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import csv
import pandas as pd


browser = webdriver.Chrome(executable_path="chromedriver.exe")
browser.get("https://www.thegioididong.com/dtdd/xiaomi-redmi-note-9s")
sleep(5)

showcomment_link = browser.find_element_by_xpath("/html/body/section/div[5]/aside[1]/div[6]/div[1]/a")
showcomment_link.click()
sleep(5)

data = []
comment_list = browser.find_element_by_xpath("//*[@id='boxRatingCmt']/div[3]/div[5]/ul[2]")
all_li = comment_list.find_elements_by_css_selector(".par.isBuy")
for li in all_li:
    content = li.find_element_by_class_name("rc").text
    #print(content, "\n")
    data.append(content)
    
#sleep(5)
df = pd.DataFrame(data)
print(df.head())

df.to_csv('data_tgdd.csv', encoding='utf-8')
browser.close()


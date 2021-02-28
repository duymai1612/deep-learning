from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import csv
import pandas as pd
import urllib
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np

def get_tags_from_url (url, class_to_find, tag_to_find):
    # erpGoogle = "https://www.thegioididong.com/"
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
    r =urllib.request.urlopen(req) 
    soup = BeautifulSoup(r, 'html.parser')
    all_tags = soup.find_all(tag_to_find,class_=class_to_find)
    # print (all_tags)
    return all_tags


# erpGoogle = "https://www.thegioididong.com/"
all_products_homepage = get_tags_from_url("https://www.thegioididong.com/", "item" , "div")
# req = urllib.request.Request(erpGoogle, headers={'User-Agent' : "Magic Browser"})
# r =urllib.request.urlopen(req) 
# soup = BeautifulSoup(r, 'html.parser')
# all_products_homepage = soup.find_all('div',class_="item")
# print(all_products_homepage[0])
list_of_comments = []
list_of_ratings = []
for product in all_products_homepage:
    # soup = BeautifulSoup(product, 'html.parser')
    # print()
    urls_to_find = product.find_all('a' )
    for link in urls_to_find:
        product_page_url = "https://www.thegioididong.com/" +  link.get("href")
        try :
            if (link.get("href").find("thegioididong.com") == -1) :
                # print(product_page_url)
                if (len(comments_url) != 0) :
                    see_all_comments_url = comments_url[0].get("href")
                    comments_of_product = get_tags_from_url ("https://www.thegioididong.com/" + see_all_comments_url, "par", "li")
                    for comment in comments_of_product:
                        
                        product_comment = comment.find("div", "rc")
                        comment_to_find = product_comment.find_all("i")
                        rating_to_find = product_comment.find("span")
                        rating_to_find = rating_to_find.find_all("i", "iconcom-txtstar")
                        list_of_comments.append(comment_to_find[5].string)
                        list_of_ratings.append(rating_to_find)
                        print (comment_to_find[5].string)
                        print (len(rating_to_find))
                
            else :
                # comments_url = get_tags_from_url (product_page_url, "rtpLnk", "a")
                comments_url = get_tags_from_url (link.get("href"), "rtpLnk", "a")
                # comments_of_product = product.find_all("ul", "ratingLst")
                # print (link.get("href"))
                if (len(comments_url) != 0) :
                    # print ("run")
                    see_all_comments_url = comments_url[0].get("href")
                    # comments_url = get_tags_from_url (product_page_url + link.get("href"), "rtpLnk", "a")
                    comments_of_product = get_tags_from_url ("https://www.thegioididong.com/" + see_all_comments_url, "par", "li")
                    for comment in comments_of_product:
                        
                        product_comment = comment.find("div", "rc")
                        comment_to_find = product_comment.find_all("i")
                        rating_to_find = product_comment.find("span")
                        rating_to_find = rating_to_find.find_all("i", "iconcom-txtstar")
                        list_of_comments.append(comment_to_find[5].string)
                        list_of_ratings.append(len(rating_to_find))
                        print (comment_to_find[5].string)
                        print (len(rating_to_find))
        except : 
            continue
        # print (comments_url)
    
    # print (url_to_find)
# data = []
# comment_list = browser.find_element_by_xpath("//*[@id='boxRatingCmt']/div[3]/div[5]/ul[2]")
# all_li = comment_list.find_elements_by_css_selector(".par.isBuy")
# for li in all_li:
#     content = li.find_element_by_class_name("rc").text
#     #print(content, "\n")
    # data.append(content)
    
# #sleep(5)
df = pd.DataFrame( {'comments': list_of_comments,
     'ratings': list_of_ratings
    })
print(df.head())

df.to_csv('D:\Deep Learning\deep-learning\Dataset\data_tgdd_from_homepage.csv', encoding='utf-8')

# browser.close()


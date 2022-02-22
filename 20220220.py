#!/usr/bin/env python
# coding: utf-8

# In[58]:


import requests
from bs4 import BeautifulSoup # HTML 빠르게 파싱 가능 (정적 페이지 분석)
from selenium import webdriver
import time
import re

from google_play_scraper import app

browser = webdriver.Chrome("chromedriver.exe")
browser.maximize_window()

url = "https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9BUFBMSUNBVElPThAHGAM%3D:S:ANO1ljKs-KA&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX0FQUExJQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljL40zU&hl=ko&gl=US"
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'lxml')

interval = 2

page_height = browser.execute_script("return document.body.scrollHeight") # 페이지 높이 저장
# print(page_height)

# 화면 맨 아래로 스크롤하도록 구현
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") # 현재 페이지에서 맨 아래로 스크롤 내리기 (아마 해상도 높이 만큼 내려갈걸)
    time.sleep(interval) # 2초동안 페이지 로딩 대기
    
    curr_height = browser.execute_script("return document.body.scrollHeight") # 현재 페이지 높이 저장
    if curr_height == page_height:
        break
    
    page_height = curr_height


app_id_list = [] 

# apps_title = soup.find_all("div", attrs={"class":"b8cIId ReQCgd Q9MA7b"})
apps_title = soup.select("div.b8cIId.ReQCgd.Q9MA7b > a")

for i in apps_title:
    id = i.attrs["href"]
    app_id_list.append(id[23:])
    
# print(app_id_list)

for j in app_id_list:
    
    result = app(j,
        lang='ko'
    )
    print(result)


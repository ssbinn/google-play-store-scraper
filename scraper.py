# 날짜: 2022.02.22

import requests
from bs4 import BeautifulSoup 
from selenium import webdriver
import time
import re
import pandas as pd
from google_play_scraper import app


url = "https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9BUFBMSUNBVElPThAHGAM%3D:S:ANO1ljKs-KA&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX0FQUExJQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljL40zU&hl=ko&gl=US"

# ---스크롤 함수---
interval = 0.8
def scrolling():
    try:
        last_height = driver.execute_script("return document.body.scrollHeight") # 페이지 높이 저장
        
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") # 현재 페이지에서 맨 아래로(해상도 높이만큼) 스크롤 내리기
            time.sleep(interval) # 2초동안 페이지 로딩 대기

            curr_height = driver.execute_script("return document.body.scrollHeight") # 현재 페이지 높이 저장
            if curr_height == last_height:
                break

            last_height = curr_height

    except Exception as e:
        print("error occurred: ", e)

        
# ---HTML 데이터 가져오기---
driver = webdriver.Chrome("chromedriver.exe")
driver.maximize_window()
driver.get(url)

scrolling() # 페이지 맨 아래로 스크롤
soup = BeautifulSoup(driver.page_source, 'html.parser') # HTML 파싱하기

apps = soup.find_all("div", attrs={"class":"b8cIId ReQCgd Q9MA7b"}) # 이 div 태그 아래에 있는 a 태그를 읽어오기 위함
# print(len(apps)) # 200개 모두 출력됨 

app_id_list = [] 

for i in apps:
    link = i.find("a")["href"]
    app_id_list.append(link[23:])

start = time.time()

# us, id 뽑아온 이유 설명 추가하기
for app_id in app_id_list:
    result = app(app_id,
        lang='ko',
        country='us'
    ) 
    print(result)

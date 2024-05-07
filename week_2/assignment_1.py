# Selenium과 Python을 이용해 임의의 페이지 3개에 접근하기
# 접근한 페이지들의 타이틀을 title 리스트에 추가하기
# 접근한 페이지들의 url을 url 리스트에 추가하기
# title 리스트와 url 리스트를 출력하는 코드 작성하기

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
pages = ['https://www.google.co.kr/',
         'https://www.naver.com/', 'https://www.daum.net/']

title = []
link = []

for url in pages:
    driver.get(url)
    title.append(driver.title)
    link.append(driver.current_url)

driver.quit()
print(title)
print(link)
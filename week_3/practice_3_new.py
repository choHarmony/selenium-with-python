import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains as AC

title_not_exist = input("존재하지 않는 영화의 제목을 쉼표로 구분하여 입력하세요.").split(',')
title_korean = input("한글 제목인 영화 제목을 쉼표로 구분하여 입력하세요.").split(',')
title_english = input("영어 제목인 영화 제목을 쉼표로 구분하여 입력하세요.").split(',')
title_special_letter = input("특수문자가 포함된 영화 제목을 쉼표로 구분하여 입력하세요.").split(',')

driver = webdriver.Chrome()
driver.get('https://www.cgv.co.kr')


def find_movie(title):
    search_box = driver.find_element(By.CSS_SELECTOR, '#header_keyword')
    search_btn = driver.find_element(By.CSS_SELECTOR, '#btn_header_search')

    search_box.click()
    search_box.send_keys(title)
    search_btn.click()
    time.sleep(3)


# 존재라지 않는 영화 이름을 검색
for i in range(len(title_not_exist)):
    find_movie(title_not_exist[i])


# 한글 영화 이름을 검색
for i in range(len(title_korean)):
    find_movie(title_korean[i])


# 영문 영화 이름을 검색
for i in range(len(title_english)):
    find_movie(title_english[i])


# 특수문자가 포함된 영화 이름을 검색
for i in range(len(title_special_letter)):
    find_movie(title_special_letter[i])


# 영화 상세 정보로 이동
if driver.title[:7] == "검색결과 없음":
    print("검색 결과가 없습니다.")
else:
    # 검색 결과가 있을 경우 나온 영화 리스트를 클릭
    movie_list = driver.find_element(
        By.CLASS_NAME, 'searchingMovieResult_list')
    movie_list.click()
    time.sleep(3)


# cgv 로고를 클릭하여 초기 화면으로 돌아감
logo = driver.find_element(
    By.CSS_SELECTOR, '#cgvwrap > div.header > div.header_content > div > h1 > a > img')
logo.click()

time.sleep(3)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://comic.naver.com/index')
driver.implicitly_wait(5)

search_box = driver.find_element(
    By.CLASS_NAME, 'SearchBar__search_input--k5nfk')
search_btn = driver.find_element(By.CLASS_NAME, 'SearchBar__btn_search--SsL7v')
search_box.click()

search_box.send_keys('이런 이름의 웹툰은 없겠지?')
search_btn.click()
search_box.clear()
time.sleep(3)

search_box = driver.find_element(
    By.CLASS_NAME, 'SearchBar__search_input--k5nfk')
search_btn = driver.find_element(By.CLASS_NAME, 'SearchBar__btn_search--SsL7v')
search_box.click()

search_box.send_keys('마루는 강쥐')
search_btn.click()
time.sleep(3)

# 검색해서 나온 웹툰의 썸네일 클릭 (상세페이지로 이동을 위해)
thumbnail = driver.find_element(By.CLASS_NAME, 'Poster__thumbnail_area--gviWY')
thumbnail.click()
time.sleep(3)

# 웹툰 상세 페이지에 '관심 웹툰 추가' 버튼 노출 여부 확인
fav_webtoon = driver.find_element(
    By.CLASS_NAME, 'EpisodeListUser__favorite--DzoPt')
if fav_webtoon.is_displayed:
    print('상세 페이지로 이동 성공')
else:
    print('상세 페이지로 이동 실패')

# 버튼 클릭 후 네이버 웹툰 메인 이동 여부 확인
main_btn = driver.find_element(By.CLASS_NAME, 'BrandBar__logo_comic--oR6mr')
main_btn.click()
time.sleep(3)

popular_webtoon = driver.find_element(
    By.CSS_SELECTOR, '#container > div.content_wrap > div.Aside__aside_wrap--iF5ju.Aside__type_home_logout--R6qSd > div:nth-child(2) > div > div.ComponentHead__title_area--IEQEG > h2 > span')
if popular_webtoon.is_displayed:
    print('테스트 완료')
else:
    print('메인 이동 실패')
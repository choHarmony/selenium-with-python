import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains as AC

driver = webdriver.Chrome()
driver.get('https://www.cgv.co.kr')

search_box = driver.find_element(By.CSS_SELECTOR, '#header_keyword')
search_btn = driver.find_element(By.CSS_SELECTOR, '#btn_header_search')
search_box.click()

# 존재하지 않는 영화 이름을 검색창에 입력
search_box.send_keys('인사이드 인')
# 검색 버튼 누르기
search_btn.click()
# 존재하지 않는 영화 검색 시 결과 페이지 확인
time.sleep(3)


search_box = driver.find_element(By.CSS_SELECTOR, '#header_keyword')
search_btn = driver.find_element(By.CSS_SELECTOR, '#btn_header_search')
# 한글 영화 이름을 검색
search_box.click()
search_box.send_keys('겨울왕국')
search_btn.click()
time.sleep(3)  # 결과 확인을 위한 명시적 대기


search_box = driver.find_element(By.CSS_SELECTOR, '#header_keyword')
search_btn = driver.find_element(By.CSS_SELECTOR, '#btn_header_search')
# 영문 영화 이름을 검색
search_box.click()
search_box.send_keys('Inside Out')
search_btn.click()
time.sleep(3)


search_box = driver.find_element(By.CSS_SELECTOR, '#header_keyword')
search_btn = driver.find_element(By.CSS_SELECTOR, '#btn_header_search')
# 특수문자가 포함된 영화 이름을 검색
search_box.click()
search_box.send_keys('Inside out!')
search_btn.click()
time.sleep(3)


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
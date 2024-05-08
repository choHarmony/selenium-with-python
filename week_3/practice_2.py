from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 원하는 특정 페이지에 접속하기
driver = webdriver.Chrome()
driver.get('https://www.cgv.co.kr')

# 묵시적으로 대기하여 페이지 로딩 기다리기
driver.implicitly_wait(10)

# 페이지가 로딩되면 임의의 엘리먼트를 지정하여 원하는 속성 출력
elem = driver.find_element(By.CSS_SELECTOR, '#btn_allView_Movie')
print(elem.get_attribute('href'))


# 다른 페이지로 이동
driver.get('https://www.naver.com/')

# 명시적 대기를 사용해 원하는 요소의 속성 출력하기
ele = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, 'MobileButtonView-module__link_mobile_v___Ptkx7'))
)
ele = driver.find_element(
    By.CLASS_NAME, 'MobileButtonView-module__link_mobile_v___Ptkx7')
print(ele.get_attribute('href'))

# 코드가 끝난 뒤 브라우저가 n초간 꺼지지 않도록 time.sleep()으로 코드 진행을 멈추기
time.sleep(5)
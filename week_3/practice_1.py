from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 원하는 특정 페이지에 접속하기
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.naver.com')
driver.implicitly_wait(10)

# inspector을 이용해 원하는 element의 클래스 값을 찾아줌
elem = driver.find_element(
    By.CLASS_NAME, 'RightSecond-module__papago_text___VLGlw')  # 네이버 메인 파파고 번역 버튼 클래스

# get_attribute 메소드를 통해 elem에서 href 속성을 찾기
att_name = elem.get_attribute('href')
if att_name == None:
    print("속성 값이 없습니다.")
else:
    print(att_name)

# elem의 텍스트 출력하기
elem_text = elem.text
if elem_text == None:
    print("텍스트가 없습니다.")
else:
    print(elem_text)

# elem의 location 출력하기
elem_loc = elem.location
print(elem_loc)

# elem location의 key를 각각 호출하여 value 값을 출력하기
print(elem_loc['x'])
print(elem_loc['y'])
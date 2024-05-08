import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://www.cgv.co.kr')

# 브라우저에서 원하는 element 위치를 알아내기
# time.sleep(3)  # 잠깐 멈춰있는 동안 마우스 커서를 element에 올려두기
# pos = pyautogui.position()  # 해당 위치 좌표 알아내기
# print(pos)

pyautogui.click(1257, 542)  # 검색창 클릭
pyautogui.typewrite('zootopia')  # 검색창에 영화 이름 입력
pyautogui.press('enter')  # 엔터키 눌러서 검색

time.sleep(3)
driver.fullscreen_window()

# fullscreen으로 해도 포스터 안 보여서 화면 축소 단축키 3번 눌러서 보이게 해줌
pyautogui.keyDown('ctrl')
for i in range(3):
    pyautogui.press('-')
pyautogui.keyUp('ctrl')

# 포스터 좌표
# 377, 446
# 707, 955

# 스크린샷 바탕화면에 저장
dest = 'C:/Users/조화수/Desktop/'  # 경로
pyautogui.screenshot(dest + 'zootopia.png', region=(377, 446, 330, 509))

# 해당 이미지 위치 인식
poster_pos = pyautogui.locateOnScreen(dest + 'zootopia.png')

# 상단 코드를 통해 인식된 위치를 토대로 해당 위치 클릭
pyautogui.click(poster_pos[0]+30, poster_pos[1]+30)

time.sleep(7)
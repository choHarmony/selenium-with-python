import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://comic.naver.com/index')
driver.implicitly_wait(5)

title_list = ['마루는 강쥐', 'ㅇ랑너ㅣㅏ', '대학일기', '미ㅏㅇㄹ', '대학원 탈출일지']
tc_count = len(title_list)
test_success = []
test_fail = []

search_box = driver.find_element(
    By.CLASS_NAME, 'SearchBar__search_input--k5nfk')
search_btn = driver.find_element(By.CLASS_NAME, 'SearchBar__btn_search--SsL7v')

for title in title_list:
    search_box.click()
    search_box.clear()
    search_box.send_keys(title)
    search_btn.click()
    time.sleep(3)

    # 검색해서 나온 웹툰의 title 클릭 (상세페이지로 이동을 위해)
    # 제목 입력이 잘못되어 아무 element도 뜨지 않을 경우를 대비하여 예외처리를 해줌
    try:
        t = driver.find_element(
            By.CSS_SELECTOR, '#content > div.component_wrap.type0 > ul > li > div > a > span > em')
        t.click()
        time.sleep(3)
    except:
        print(f'{title} : 웹툰 제목을 확인해주세요.')
        test_fail.append(title)
        continue

    # 웹툰 상세 페이지에 '관심 웹툰 추가' 버튼 노출 여부 확인
    # if문을 통해 성공적으로 로딩되었는지 여부 확인
    fav_webtoon = driver.find_element(
        By.CLASS_NAME, 'EpisodeListUser__favorite--DzoPt')
    if fav_webtoon.is_displayed:
        print(f'{title} : 상세 페이지로 이동 성공')
        test_success.append(title)
    else:
        print('상세 페이지로 이동 실패')

print(test_success)
print(test_fail)


# 테스트 결과 리포트 만들기

# 바탕화면에 'test_result' 폴더가 없으면 만들어라
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') # 바탕화면 경로
folder_path = os.path.join(desktop_path, 'test_result') # 바탕화면 경로 + 만들 report 파일명

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# report 파일 만들기 (파일 없으면 만들고, 있으면 내용 덮어쓰는 모드)
report = open(desktop_path + '/test_result/webtoon_test_report.txt', 'x')

# 테스트를 마친 후 report 작성
report.write(time.strftime('%Y-%m-%d %H:%M')+'\n')
report.write(f'PASS TITLE LIST : {test_success}\n')
report.write(f'FAIL TITLE LIST : {test_fail}\n')
report.write(f'PASS RATE : {len(test_success) / tc_count * 100}%')
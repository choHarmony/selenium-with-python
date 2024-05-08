# 네이버 뉴스 메인 페이지의 html 데이터를 가져오기
import requests

response = requests.get('https://news.naver.com/')

print(response.text)
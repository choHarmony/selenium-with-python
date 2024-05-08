import requests

code = []

for i in range(3):
    response = requests.get(input('웹 페이지를 입력하세요. '))
    code.append(response.status_code)

print(code)
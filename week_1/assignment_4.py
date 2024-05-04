# 1~10 사이의 정수 1개를 입력받아 해당 구구단 단을 출력하기
num = int(input())

if num > 10:
    print("1~10 사이의 정수를 입력해주세요.")

else:
    for i in range(1, 10):
        print(f'{num} X {i} = {num*i}')
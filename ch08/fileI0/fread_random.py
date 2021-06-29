# kbo 구단을 1개씩 랜덤 추출하기
import random

try:
    f = open('c:/pyfile/2021kbo.txt', 'r')
    data = f.read().split() #공백문자로 구분
    team = random.choice(data)
    print(team)

    f.close()
except FileNotFoundError as e:
    print(e)
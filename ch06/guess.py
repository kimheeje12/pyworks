# 숫자를 추측해서 맞히는 프로그램

import random

com = random.randint(1, 30) # 컴이 추측 숫자
while True:
    guess = int(input("맞혀보세요(1~30): "))
    if guess == com:
        print("정답!")
    elif guess > com:
        print("너무 커요!")
    else:
        print("너무 작아요!")

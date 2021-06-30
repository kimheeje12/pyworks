# 숫자를 추측해서 맞히는 프로그램

import random
com = random.randint(1, 30) # 컴이 추측 숫자
while True:
    try:
        guess = int(input("맞혀보세요(1~30): ")) # 사용자가 추측 숫자
        if guess == com:
            print("정답!")
            break
        elif guess > 30 or guess < 1:
            print("게임 범위를 초과하였습니다. 다시 입력해주세요.")
        elif guess > com:
            print("너무 커요!")
        else:
            print("너무 작아요!")
    except ValueError:
        print("숫자가 아닙니다. 다시 입력해주세요. ")



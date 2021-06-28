# 주사위 2개를 10번 던지기
# 두 눈의 합이 7이면, Seven Thrown 출력 / 11이면, Eleven Thrown 출력 /
# 두 눈의 수가 같으면 Double Thrown!! 출력

import random

for i in range(10):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print(total)
    if total == 7:
        print("Seven Thrown")
    if total == 11:
        print("Eleven Thrown")
    if dice1 == dice2:
        print("Double Thrown!!")

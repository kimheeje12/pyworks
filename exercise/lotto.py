import random
'''
for i in range(0, 10):
    n = random.randint(1, 6)
    dice.append(n)

#print(dice)
'''
# 로또 복권 생성기
lotto = []
while len(lotto) < 6:
    print(len(lotto))
    n = random.randint(1, 45)
    if n not in lotto:
        lotto.append(n)

print(lotto)
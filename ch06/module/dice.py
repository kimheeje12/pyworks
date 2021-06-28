import random

# 주사위 10번 던지기
'''
for i in range(10):
    dice = random.randint(1, 6)
    print(dice)

print('='*40)
'''

# 리스트에서 랜덤하게 단어 추출하기
word = ['sky', 'moon', 'space', 'earth']
w = random.choice(word)
print(w)

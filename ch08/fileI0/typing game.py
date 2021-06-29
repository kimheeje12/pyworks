# 영어 타자 연습 프로그램
import random
import time

f = open('words.txt', 'r')
word = f.read().split() # 리스트 형태로 가져옴
# print(word)
f.close()

n = 1 # 문제 번호
print("[타자 게임]준비되면 엔터")
input()
start = time.time()
q = random.choice(word) # 단어 랜덤 선택
while n <= 10:
    print("문제", n)
    print(q)
    x = input() # 사용자가 단어를 따라 입력
    if q == x:
        print("통과")
        n = n + 1
        q = random.choice(word)
    else:
        print("오타! 다시 도전")
    #n = n + 1

end = time.time()
et = end - start
print("타자 시간 : %.2f초" % et)
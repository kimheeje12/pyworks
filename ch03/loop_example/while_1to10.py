# 1부터 10까지 출력하기

i = 1
sum = 0
while i < 11:
    sum += i
    #print(i, end=' ') # 수평 출력
    print("i= ", i, ", sum = ", sum)
    i += 1

print("합계: ", sum)

# 리스트의 연산
score = [70, 80, 50, 60, 90, 45]
sum = 0
avg = 0.0
count = len(score)

# 합계
for i in score:
    sum += i
    print("i=%d, sum=%d" % (i, sum)) 

# 평균
avg = sum / count

#print("개수 : %d개" % count)
print("개수 : {}개".format(count))
#print("합계 : %d점" % sum)
print("합계 : {}점".format(sum))
print("평균 : %.1f점" % avg)

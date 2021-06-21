# 리스트의 합격 판정
# 점수가 60점 이상이면 합격, 불합격

print("for - in문 사용")
score = [70, 80, 50, 60, 90, 45]
index = 0
for i in score:
    index += 1
    if i >= 60:
        print("%d번 학생은 합격입니다." % index)
    else:
        print("%d번 학생은 불합격입니다." % index)

print('='*40)

print("for in range() 구문")

n = len(score)
for i in range(0, n):
    if score[i] >= 60:
       print("%d번 학생은 합격입니다." % (i+1)) #대응변수 괄호로 묶음
    else:
        print("%d번 학생은 불합격입니다." % (i+1))

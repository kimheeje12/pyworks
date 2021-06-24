# 1번

kor = 80
eng = 75
math = 55
sum = kor + eng + math 
avg = sum / 3
print("홍길동 씨의 평균점수: ", avg)

'''
국어 = 80
영어 = 75
수학 = 55

평균 = (국어 + 영어 + 수학) /3

print("평균: ", 평균)
'''

# 2번
'''print(13 % 2)'''
n = 13
if n % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 3번 ~ 4번
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

gender = pin[7]
'''print(gender) #성별 구분 문자  '''
if gender == "1":
    print("남자입니다")
else:
    print("여자입니다")

# 5번
a = "a:b:c:d"
b = a.replace(':', '#')
print(b)

# 6번
a = [1, 3, 5, 4, 2]
a.sort() # 오름차순 정렬
a.reverse() # 내림차순 정렬
print(a)

# 7번
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

# split() 예제
msg = "Life is too short"
msg = msg.split() # 구분기호 : 공백
print(msg)

s = "a:b:c:d"
s = s.split(':')
print(s)

# 8번
a = (1, 2, 3)
a = a + (4,)
print(a)

# 9번
a = dict() # 빈 딕셔너리
print(a)
a['name'] = 'python'
print(a)
a[('a')] = 'python'
print(a)
#a[[1]] = 'python'
#print(a)
a[250] = 'python'
print(a)

# 10번
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

# 11번
a = [1, 1, 1, 2, 2, 3, 3, 3 ,4, 4, 5]
aSet = set(a) # 중복 제거
b = list(aSet) # list형으로 변환
print(b)

# 12번
a = b = [1, 2, 3]
a[1] = 4
print(b)











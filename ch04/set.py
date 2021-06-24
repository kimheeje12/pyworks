# set() 자료구조 특징
# 순서가 없고, 중복이 허용되지 않음

s = set() #빈 집합 자료형 선언
s.add(1)
s.add(2)
print(s)

#중복저장 안됨
s2 = set(['cow', 'dog', 'cat', 'dog'])
print(s2)

#리스트와 비교(중복저장 ok)
ani = ['cow', 'dog', 'cat', 'dog']
print(ani)

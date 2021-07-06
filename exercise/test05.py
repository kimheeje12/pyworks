'''
# 1번
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
        return self.value

# 2번
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
        return self.value

# 부모 클래스의 인스턴스
c = Calculator()
print(c.add(10))
print(c.value)

cal = UpgradeCalculator()
print(cal.add(10))
print(cal.minus(7))
print(cal.value)

cal2 = MaxLimitCalculator()
print(cal2.add(50))
print(cal2.add(60))
print(cal2.value)
'''

# 3번(shell에서 체크)
import datetime

'''
# 4번
def postitive(a):
    a2=[]
    for i in a:
        if i >= 0:
            a2.append(i)
    return a2

li2= [1, -2, 3, -5, 8, -3]
li = positive(li2)
print(li)
'''
#print(list(filter(lambda x : x >= 0, li)))

# 6번
def times(a):
    a2 = []
    for i in a:
        a2.append(i*3)
    return a2

li = [1, 2, 3, 4]

print(list(map(lambda x : x*3, li)))

# 7번
def find_max(li):
    max = li[0]
    for i in li:
        if max < i:
            max = i
    return(max)

    '''
    n = len(li)
    for i in range(1, n):
        print(max)
        if max < li[i]:
            max = li[i]
    '''
    return(max)

# max값 구하기
d1 = [-8, 2, 7, 5, -3, 5, 0, 1]
max = max(d1)
min = min(d1)
print(max)
print(min)
print(max+max)
print(min+min)

# 8번
# console
# round(17/3, 4)
# 내림은 import math, math.floor(17/3)

# 9번
# myargv

# 10번
# os

# 11번
# glob

# 12번
# time 모듈 사용
import time
now1 = datetime.datetime.now()
print(now1.strftime("%Y/%m/%d %H:%M:%S"))

now2 = time.strftime("%Y/%m/%d %H:%M:%S")
print(now2)

# 13번
# 정규 표현식 예제
import re

str = "Two is too"
f1 = re.findall("T[ow]o", str) # 대소문자 구분
print(f1)

f2 = re.findall("T[ow]o", str, re.IGNORECASE) # 대소문자 구분하지 않음
print(f2)

f3 = re.findall("t[^w]o", str, re.IGNORECASE)
print(f3)

'''
p = re.compile('ca+t') # +는 반복을 의미하는 메타 문자
m = p.match('caaat')
print(m)
'''
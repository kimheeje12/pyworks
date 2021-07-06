# 정규 표현식 예제
import re

#p = re.compile('a.b') # .은 임의의 문자 1개 메타 문자
p = re.compile('a+b') # +는 앞문자 1개 이상 이메타 문자
m = p.match('aaaab')
print(m.group())

# match(): 처음부터 문자를 검색 = find()와 비슷
# findall(): 전체를 검색해서 리스트로 반환 = findall()

'''
p = re.compile('[a-z]+') # +는 반복을 의미하는 메타 문자
m = p.match('afternoon')
print(m)
'''
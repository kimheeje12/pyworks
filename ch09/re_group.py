import re

# ()로 구분해서 이름과 전화번호를 분리해서 추출
p = re.compile("(\w+)\s+(\d+[-]\d{4}[-]\d{4})") # + 넣거나 {4} 넣기
s = p.search("jang 010-1234-5678")
print(s.group(1))
print(s.group(2))
print(s.group())
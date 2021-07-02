import re

p = re.compile("(\w+)\s(\d+[-]\d{4}[-]\d{4})") # + 넣거나 {4} 넣기
s = p.search("jang 010-1234-5678")
print(s.group(1))
print(s.group(2))
print(s.group())
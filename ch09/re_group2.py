import re

# 그룹핑된 문자열에 이름 붙이기
#?P<그룹이름>
p = re.compile("(?P<name>\w+)\s+(?P<phone>\d+[-]\d{4}[-]\d{4})")
s = p.search("jang 010-1234-5678")
print(s.group("name"))
print(s.group("phone"))
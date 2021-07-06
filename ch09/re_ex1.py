import re

# '*'와 '+'의 차이 비교
# '*'는 앞 문자가 0개 이상 반복(없어도 가능)
pat = re.compile("ca*t")
m1 = re.findall(pat, "caat")
print(m1)
m2 = re.findall(pat, "ct")
print(m2)

# '+'는 앞 문자가 1개 이상 반복
# pat2 = re.compile("ca+t")
m3 = re.findall("ca+t", "caat")
print(m3)
m4 = re.findall("ca+t", "ct")
print(m4)
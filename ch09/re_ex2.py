# {m} m은 반복횟수
# {m, n} m은 최소, n은 최대횟수
import re

str = "123?45yy7890 hi 999 Hello"
m1 = re.findall("\d{1,3}", str)
print(m1)

m2 = re.findall("[A-z]+", str)
print(m2)

m3 = re.findall("[1-5]{1,2}", str)
print(m3)


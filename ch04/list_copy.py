# 리스트의 복사
# a리스트 요소를 a2 리스트로 복사(저장)

a = [1, 2, 3, 4, 5, 6]
a2 = []

for i in a:
    a2.append(i*2)

print(a2)

# a 리스트의 홀수를 a3 리스트에 저장
a3 = []

for i in a:
    if i % 2 == 1:
        a3.append(i)

print(a3)

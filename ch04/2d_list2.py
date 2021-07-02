
d1 = [1, 2, 3]
print(d1[0])
d1.append(10)
print(d1)

d2 = [
    [10],
    [20],
    [30]
]
'''
print(d2[0][0])
print(d2[1][0])
print(d2[2][0])
'''
d2.append([40])
# print(d2)

for i in d2:
    print([i][0])

# d2의 합계
d2.append([d2[0][0] + d2[1][0] + d2[2][0] + d2[3][0]])
print(d2)
avg = (d2[0][0] + d2[1][0] + d2[2][0] + d2[3][0]) / 4
d2.append([avg])
print(d2)

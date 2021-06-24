# dic
person = {}
print(person)

person['name'] = "이순신"
person['age'] = 40
print(person)

person['address'] = "인천"
print(person)

# dic value 출력
for key in person:
    print(person[key])

# 요소 삭제: dic.pop('address')와 같음
del person['address']
print(person)


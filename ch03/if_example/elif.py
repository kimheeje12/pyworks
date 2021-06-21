#놀이공원 입장료 계산

age = int(input("나이를 입력해 주세요: "))

if age < 8:
    print("취학 전 아동입니다.")
    charge = 1000
elif age < 14:
    print("초등학생입니다.")
    charge = 2000
elif age < 20:
    print("중, 고등학생입니다.")
    charge = 2500
else:
    print("일반인입니다.")
    charge = 3000

print("입장료는 %d원입니다." % charge)    

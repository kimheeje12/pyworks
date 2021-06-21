#조건 : 현금이 있고, 카드가 있으면 택시를 타고, 아니면 걸어간다.

money = 3000
card = True
if money > 4000 or not card:
    print("택시를 탄다")
else:
    print("걸어 간다.")


pocket = ['paper', '스마트폰', 'money']
if 'money' in pocket:
    print('택시를 탄다')
else:
    print('걸어 간다')

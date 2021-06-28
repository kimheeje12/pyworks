import sys

print('수를 입력하세요: ')
n = int(input())
if n == 0:
    print("0으로 나눌 수 없습니다.")
    sys.exit()

print(3 / n)

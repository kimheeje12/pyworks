# while ~ break

while True:
    print("반복을 계속할까요? [y/n] : ")
    answer = input()

    if answer == 'y' or answer == 'Y':
        print("반복을 계속 합니다.")
    elif answer == 'n' or answer == 'N':
        print("반복을 중단합니다.")
        break
    else:
        print("잘못된 입력입니다.")

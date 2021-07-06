while True:
    try:
        x = int(input("숫자를 입력하세요: "))
        print(x)
        break
    except ValueError as e:
        #print(e)
        print("숫자가 아닙니다. 다시 입력해주세요")

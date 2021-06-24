# 함수의 정의 및 호출
# return이 없고 매개변수 없는 함수

def say_hello():
    print("안녕하세요!")

# return이 없고 매개변수 있는 함수
def say_hello2(name):
    print("{}님 반갑습니다.".format(name))

say_hello() # 호출
say_hello()
print('='*30)
    
say_hello2('홍길동')
say_hello2('Elsa')

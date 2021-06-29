def oneup2(x):
    return x + 1

# 매개변수가 1개 있는 lambda 함수(익명 함수)
# 1을 더하는 함수

oneup = lambda x : x + 1
print(oneup(2)) # 람다 함수 호출
print((lambda x : x + 1)(2))

# print(oneup2(2)) # 일반 함수 호출

# 3의 배수를 계산 함수
times = lambda n : n * 3
print(times(2))
print((lambda n : n * 3)(2))

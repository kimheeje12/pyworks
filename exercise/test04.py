# 1번
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

num = is_odd(11)
print(num)

# 2번
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1, 2))
print(avg_numbers(3, 2, 5, 4, 1))

'''
# 3번
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)
#print("두 수의 합은 %d 입니다" % total)
'''

# 4번
print("you" "need" "python")
print("you"+"need"+"python")
print("you","need","python")
print("".join(["you","need","python"]))

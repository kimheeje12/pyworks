
def incrementor(n):
    return lambda x : x + n

f = incrementor(10)
print(f(1))
print(f(2))

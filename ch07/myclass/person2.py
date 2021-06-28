class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("홍길동", 40)
print(p1.name, p1.age)

p2 = Person("이산", 35)
print(p2.name, p2.age)

p3 = Person("감귤", 30)
print(p3.name, p3.age)
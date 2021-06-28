from person import Person

# 멤버 매개변수가 있는 상속
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
'''
class Employee(Person):
    def __init__(self, name, age, empid):
        super().__init__(name, age)  #부모멤버는 super()를 사용
        self.empid = empid

    def getname(self): # 캡슐화(정보은닉) - get() 메서드 사용
        return self.name

    def getage(self):
        return self.age

    def getempid(self):
        return self.empid

e1 = Employee("북한산", 20, 201)
print("이름 : ", e1.getname())
print("나이 : ", e1.getage())
print("사번 : ", e1.getempid())

e2 = Employee("백두산", 25, 202)
print("이름 : ", e2.getname())
print("나이 : ", e2.getname())
print("사번 : ", e2.getname())

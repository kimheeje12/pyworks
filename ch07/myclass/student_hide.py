# 학생 클래스 생성과 사용

class Student:
    def __init__(self, sid, name):
        self.__sid = sid  #학번
        self.__name = name

    def getsid(self):
        return self.__sid

    def getname(self):
        return self.__name

s1 = Student(1001, '김산')
print(s1.getsid(), s1.getname())
s2 = Student(1002, '이강')
print(s2.getsid(), s2.getname())

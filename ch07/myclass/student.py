# 학생 클래스 생성과 사용

class Student:
    def __init__(self, sid, name):
        self.sid = sid  #학번
        self.name = name

    def showinfo(self): #정보 출력 메서드
        print(self.sid, self.name)

if __name__ == "__main__":
    s1 = Student(1001, "박대양")
    s1.showinfo()

    s2 = Student(1002, "이산")
    s2.showinfo()


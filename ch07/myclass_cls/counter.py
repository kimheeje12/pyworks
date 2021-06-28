# counter 클래스
class Counter:
    def __init__(self):
        self.x = 0 # 인스턴스 변수(heap 영역)
        self.x = self.x + 1

    def showinfo(self):
        print(self.x)

c1 = Counter()
c1.showinfo()
c2 = Counter()
c2.showinfo()
c3 = Counter()
c3.showinfo()

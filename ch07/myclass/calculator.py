# 계산기 클래스 만들기

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def div(self):
        return self.x / self.y

if __name__ == "__main__":
    c = Calculator(7, 4)
    print(c.add())
    print(c.sub())
    print(c.mul())
    print(c.div())
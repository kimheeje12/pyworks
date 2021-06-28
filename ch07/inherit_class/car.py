# Car는 부모 클래스 = Taxi, Bus가 자식 클래스
# 상속의 경우 - 메서드 재정의(오버라이딩)가 발생
class Car:
    def drive(self):
        print("차를 주행합니다.")

class Taxi(Car):
    def drive(self):
        print("택시를 주행합니다.")

class Bus(Car):
    def drive(self):
        print("버스를 주행합니다.")

c = Car()
c.drive()

taxi = Taxi()
taxi.drive()

bus = Bus()
bus.drive()
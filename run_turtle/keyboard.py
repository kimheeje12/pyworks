import turtle as t

def turn_right(): # 오른쪽 화살키
    t.setheading(0)
    t.forward(10)

def turn_up(): # 윗쪽 화살키
    t.setheading(90)
    t.forward(10)

def turn_left(): #왼쪽 화살키
    t.setheading(180)
    t.forward(10)

def turn_down(): #아랫쪽 화살키
    t.setheading(270)
    t.forward(10)

def clear():
    t.clear()

t.shape("turtle")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(clear, "Escape")

t.listen() #키보드의 동작을 기다림

t.mainloop()
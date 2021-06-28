#랜덤하게 거북이가 걸어가기

import turtle as t
import random as r

t.shape("turtle")
t.speed(0)
t.bgcolor("pink")
#t.setup(500, 500) # 작업영역(무대)의 크기

for x in range(300): # 거북이가 100번 움직임
    angle = r.randint(1, 360) # 거북이의 방향(각도) 
    t.setheading(angle)
    t.forward(10)

t.mainloop()
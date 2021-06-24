# 도형 그리기

import turtle as t

t.shape("turtle")

# 사각형 그리기
n = 4
for i in range(n):
    t.forward(100)
    t.right(360/n)

# 삼각형 그리기
n = 3
t.color('red')
t.pensize(2)
for i in range(n):
    t.forward(100)
    t.left(360/3)

# 원
t.color('blue')
t.pensize(3)
t.circle(50)

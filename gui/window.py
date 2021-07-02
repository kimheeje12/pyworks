# 윈도우(폼) 만들기

from tkinter import *

root = Tk() # Tk()클래스의 객체 생성
root.title("window")
root.geometry("200x100+300+400") # width x height + x좌표 + y좌표

frame = Frame(root) # root 위에 위치하는 프레임 객체
frame.pack() # 레이아웃 담당하는 메서드

# 문자열 출력 - Label 클래스
Label(frame, text = "Hello Python").grid(row=0, column=0)
# 버튼 클래스
Button(frame, text = "확인").grid(row=1, column=0)

root.mainloop()

from tkinter import *

def click():
    en_text = entry.get()
    text.insert(END, en_text) # END 안 넣으면 오류남

root = Tk()
root.title("Hello~") # 루트
root.geometry("200x150+200+200")

frame = Frame(root) # 프레임
frame.pack()

Label(frame, text = "이름: ").grid(row=0, column=0)
entry = Entry(frame, width=10)
entry.grid(row=0, column=1)
Button(frame, text="확인", command=click).grid(row=1, columnspan=2)
# click 다음 ()생략한 이유는 버튼 누를때만 함수 작동, () 있으면 함수 생성시점에서 동작
text = Text(frame, width=20, height=5)
text.grid(row=2, columnspan=2)

root.mainloop()
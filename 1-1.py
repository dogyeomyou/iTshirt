# -*- coding: utf-8 -*-

#code01.py
from tkinter import*

window = Tk()
window.title("test01")
window.geometry("500x500+700+200")
label = Label(window, text="파이썬에 오신것을 환영합니다")
button = Button(window, text="저를 클릭해주세요")
label.pack()
button.pack()

window.mainloop()

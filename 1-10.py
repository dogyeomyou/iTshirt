#code10.py
from tkinter import *

class MenuDemo:
    def __init__(self):
        window = Tk()
        window.title("메뉴 데모")
        
        #메뉴바를 생성한다.
        menubar = Menu(window)
        window.config(menu=menubar)
        #풀다운 메뉴를 생성하고, 메뉴바를 추가한다.
        operationMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label = "연산", menu=operationMenu)
        operationMenu.add_command(label="더하기", command=self.add)
        operationMenu.add_command(label="빼기", command=self.subtract)
        operationMenu.add_command(label="곱하기", command=self.multiply)
        operationMenu.add_command(label="나누기", command=self.divide)
        #추가적인 풀다운 메뉴를 생성한다.
        exitmenu = Menu(menubar, tearoff=0)
        menubar.add_csacade(label="나가기", menu=exitmenu)
        exitmenu.add_command(label="종료하기", command=window.quit)
        
        #툴바 프레임을 추가한다
        frame0 = Frame(window)
        frame0.grid(row1, column=1, sticky=W)
        #이미즈를 생성한다
        plusImage = PhotoImage(file="image/plus.gif", master=window)
        minusImage = PhotoImage(file="image/minus.gif", master=window)
        timesImage = PhotoImage(file="image/times.gif", master=window)
        divideImage = PhotoImage(file="image/divide.gif", master=window)
        
        button(frame0, image=plusImage,command=self.add).grid(row=1, column=1, sticky=W)
        button(frame0, image=minusImage,command=self.subtract).grid(row=1, column=2)
        button(frame0, image=timesImage,command=self.multiply).grid(row=1, column=3)
        button(frame0, image=divideImage,command=self.divide).grid(row=1, column=4)
        
        #레이블과 엔트리를 frame1에 추가한다.
        frame1 = Frame(window)
        frame1.grid(row=2, column=1, pady=10)
        
        Label(frame1, text="숫자 1:").pack(side=LEFT)
        self.v1 = StringVar()
        Entry(frame1, width=5, textvariable=self.v1, justify=RIGHT).pack(side=LEFT)
        
        Label(frame1, text="숫자 2:").pack(side=LEFT)
        self.v2 = StringVar()
        Entry(frame1, width=5, textvariable=self.v2, justify=RIGHT).pack(side=LEFT)
        
        Label(frame1, text="결과:").pack(side=LEFT)
        self.v3 = StringVar()
        Entry(frame1, width=5, textvariable=self.v3, justify=RIGHT).pack(side=LEFT)
        
        #버튼을 frame2에 추가한다
        frame2 = Frame(window)
        frame2.grid(row=3, column=1, pady=10, sticky=E)
        Button(frame2, text="더하기", command=self.add).pack(side=LEFT)
        Button(frame2, text="빼기", command=self.subtract).pack(side=LEFT)
        Button(frame2, text="곱하기", command=self.multiply).pack(side=LEFT)
        Button(frame2, text="나누기", command=self.divide).pack(side=LEFT)
        #이벤트 루프를 생성한다.
        window.mainloop()
        
    def add(self):
        print("add")
        self.v3.set(eval(self.v1.get()) + eval(self.v2.get()))
        
    def subtract(self):
        print("subtract")
        self.v3.set(eval(self.v1.get()) - eval(self.v2.get()))
            
    def multiply(self):
        print("multiply")
        self.v3.set(eval(self.v1.get()) * eval(self.v2.get()))
                
    def divide(self):
        print("divide")
        self.v3.set(eval(self.v1.get()) / eval(self.v2.get()))
        
MenuDemo()
        
        
        
        
        
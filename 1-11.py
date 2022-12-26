#code11.py

from tkinter import *

class PopupMenuDemo:
    def __init__(self):
        window = Tk()
        window.title("팝업 메뉴 데모")
        
        #팝업 메뉴를 생성한다.
        self.menui = Menu(window, tearoff=0)
        self.menu.add_command(label="선 그리기", command=self.displayLine)
        self.menu.add_command(label="타원 그리기", command=self.displayOval)
        self.menu.add_command(label="사각형 그리기", command=self.displayrect)
        self.menu.add_command(label="지우기 그리기", command=self.clearCanvas)
        
        #창에 캔버스를 배치한다.
        self.canvas = Canvas(window, width=200, height=100, bg="white")
        self.canvas.pack()
        
        #팝업을 캔버스에 연결한다.
        self.canvas.bind("<Button-3>", self.popup)
        
        window.mainloop()# 이벤트 루프를 생성한다.
        
        #사각형으로 출력한다
    def displayLine(self):
        print("line1")
        #타원으로 출력한다
        self.canvas.create_line(10,10,190,90, tags="line")
        self.canvas.create_line(20,20,190,90, tags="line")
    def displayOval(self):
        print("line2")
        self.canvas.create_oval(10,10,190,90, tags="oval")
    def displayRect(self):
        print("line3")
        self.canvas.create_rect(10,10,190,90, tags="rect")
    def clearCanvas(self):
        print("line4")
        self.canvas.delete("rect", "oval", "line")
    def popup(self, event):
        self.menu.post(event.x_root, event.y_root)
PopupMenuDemo()
        

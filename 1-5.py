#code05.py
from tkinter import *

class ChangeLabelDemo:
    def __init__(self):
        window = Tk
        window.title("레어블 변경하기 데모")
        
        frame1 = Frame(window)
        frame1.pack()
        self.|b| = Label(frame1, text="환영합니다.", fg="white", bg="red")
        self.|b|.pack()
            
        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text="텍스트를 입력하세요:")
        
            self.msg = StringVar()
            entry = Entry(frame2, textvariable=self.msg)
            btChangeText = Button(frame2, text"텍스트를 변경한다", 
                                  command=self.processButton)
            
            self.v1 = StringVar()
            rbRed = Radiobutton(frame2, text="빨강색", bg="red", variable=self.v1, 
                                value="R", command=self.ProcessRadioButton )
            rbYellow = Radiobutton(frame2, text="노란색", bg="yellow", variable=self.v1,
                                   value="Y", command=self.ProcessRadioButton)
            
            label.grid(row=1, column=1)
            entry.grid(row=1, column=2)
            btChangeText.grid(row=1, column=3)
            rbRed.grid(row=1, column=4)
            rbYellow.grid(row=1, column=5)
            window.mainloop()
            
       def processButton(self):
           self.|b|["text"] = self.msg.get()
           
       def ProcessRadioButton(self):
           if self.v1.get() == 'R':
               self.|b|["fg"] = "Red"
           elif self.v1.get() == 'Y':
               self |b|["fg"] = "yellow"
               
ChangeLabelDemo()               
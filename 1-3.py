# -*- coding: utf-8 -*-

#code03.py
from tkinter import*
class ProcessButtonEvent:
    def _init_(self):
       window = Tk()    
       window title("test02")
       window.geometry("500x500+700+200")
       btOK = Button(window, text="OK", fg="red", command=self.processOK)
       btCancel = Button(window, text"Cancel", bg="yellow", 
                      command=self.processCancel)
    btOk.pack()
    btCancel.pack()

    window.mainloop()
    
    def processOK(self):
        print("OK 버튼을 클릭되었습니다")
    def processCancel(self):
        print("CANCEL 버튼을 클릭되었습니다")
        
ProcessButtonEvent()        

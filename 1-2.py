#code02.py
from tkinter import *

def processOK():
    print("OK 버튼이 클릭되었습니다.")
    
def processCancel():
    print("Camcel 버튼이 클릭되었습니다.")

window = Tk()
btOK = Button(window, text = "OK", fg="red", command = processOK)   
btCancel = Button(window, text = "Cancel", fg="yellow", command = processCancel)  
btOK.pack()
btCancel.pack()

window.mainloop()



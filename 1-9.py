# -*- coding: utf-8 -*-

#code09.py
from tkinter import *

class imageDemo:
    def __init__(self):
        window = Tk()
        window.title("이미지 데모")
        
        koreaimage = Photoimage(file= "korea.gif")
        chinaimage = Photoimage(file= "china.gif")
        leftimage = Photoimage(file= "Larrow.gif")
        rightimage = Photoimage(file= "Rarrow.gif")
        
        frame1=Frame(window)
        frame1.pack()
        Label(frame1, image=koreaimage).pack(side=LEFT)
        canvas = Canvas(frame1)
        canvas.create_image(500,400, image=chinaimage)
        canvas["width"] = 500
        canvas["height"] = 400
        canvas.pack(side=LEFT)
        
        frame2 = frame(Windows)
        frame2.pack()
        Button(frame2, image=leftimage).pack(side=LEFT)
        Button(frame2, image=rightimage).pack(side=LEFT)
        
        window.mainloop()
        
imageDemo()        

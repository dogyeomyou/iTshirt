# -*- coding: utf-8 -*-
#four07.py
from tkinter import *

class FanRotateDemo:
    def __init__(self):
        window = Tk()
        window.title("작동하고 있는 팬 출력하기")
        window.geometry("300x300")
        
        self.canvas = Canvas(window)
        self.canvas.pack()
        
        self.fanSpeed = 10
        self.starts = [0, 90, 180, 270]
        self.s0, self.s1, self.s3 = 0, 90, 180. 270
        print(self.s0, self.s1, self.s2, self.s3)
        self.canvas.create_arc(50, 50, 250,250, start=self.s0, extent20,
            fill="black", tags="arc")
        self.canvas.create_arc(50, 50, 250,250, start=self.s1, extent20,
            fill="black", tags="arc")
        self.canvas.create_arc(50, 50, 250,250, start=self.s2, extent20,
            fill="black", tags="arc")
        self.canvas.create_arc(50, 50, 250,250, start=self.s3, extent20,
            fill="black", tags="arc")
        self.canvas.after(100)
        self.canvas.update()
        
        self.animate()
        
        window.mainloop()
        
     def animate(self):
         
         for i in range(100):
             self.canvas.delete("arc")
             self.s0 += self.fanSpeed
             self.s1 += self.fanSpeed
             self.s2 += self.fanSpeed
             self.s3 += self.fanSpeed
             self.canvas.create_arc(50, 50, 250,250, start=self.s0, extent20,
                 fill="black", tags="arc")
             self.canvas.create_arc(50, 50, 250,250, start=self.s1, extent20,
                 fill="black", tags="arc")
             self.canvas.create_arc(50, 50, 250,250, start=self.s2, extent20,
                 fill="black", tags="arc")
             self.canvas.create_arc(50, 50, 250,250, start=self.s3, extent20,
                 fill="black", tags="arc")
             self.canvas.after(100)
             self.canvas.update()
             
FanRotateDemo()
             
             
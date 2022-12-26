# -*- coding: utf-8 -*-

from tkinter import *

class Chess:
    def __init__(self):
        window = Tk()
        window.title("체스판")
        window.geometry("500x500+700+200")
        
        self.chess_size = 8
        self.width = 400
        self.height = 400
        self.canvas = Canvas(window, bg="white", width=self.width, height=self.height)
        self.canvas.pack()
        
        for self.i in range(self.chess_size):
            print()
            for self.j in range(self.chess_size):
            self.drawChess(self.i, self.j) #각 행마다
                
     window.mainloop()

     def drawChess (self, x, y):
         dx = 50
         dy = 50 
         side = 50
         #print(x,y)
         if (x+y)%2 == 0: # 짝수
            y *= dx
            x *= dy
            x1, y1 = x, y
            x2, y2 = x+side, y+side
            print("R",x1,y1, x2,y2, end=" ")
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", tags="rect")
        else: # 홀수 
          y *= dx
          x *= dy
          x1, y1 = x, y
          x2, y2 = x+side, y+side
          print("B", x1,y1, x2,y2, end" ")
          self.canvas.create_rectangle(x1, y1, x2, y2, fill="black", tags="rect")
          
          chess()
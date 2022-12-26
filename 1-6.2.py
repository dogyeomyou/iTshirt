# -*- coding: utf-8 -*-

#copy06.py
from tkinter import *

class CanvasDemo:
  def __init__(self):
     window = Tk()
     window.title("Canvas Demo")

     self.canvas = Canvas(window, width=400, height=400, bg="white")
     self.canvas.pack()

     frame = Frame(window)
     frame.pack()
    
     btOval = Button(frame, text="타원", command=self.displayOval)
     btLine = Button(frame, text="선분", command=self.displayLine)
     btClear = Button(frame, text="삭제하기", command=self.clearCanvas)

     btOval.grid(row = 1, column = 1)
     btLine.grid(row = 1, column = 2)
     btClear.grid(row = 1, column = 3)

     window.mainloop()
     
     def displayOval(self):
        self.canvas.create_oval(100, 100, 300, 300, fill="yellow", tags="oval")

     def displayLine(self):
        self.canvas.create_line(200, 100, 200, 300, fill = "red", tags="line")
        self.canvas.create_line(100, 200, 300, 200, fill="red", tags="line")

     def clearCanvas(self):
        self.canvas.delete("oval", "line")
    
     CanvasDemo()

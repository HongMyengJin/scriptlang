from tkinter import *
class Cell(Canvas):
    def __init__(self, parent, row, col, width = 20, height = 20):
        Canvas.__init__(self, parent, width = width, height = height, \
        bg = "blue", borderwidth = 2)
        self.color = "white"
        self.row = row
        self.col = col
        # https://tkdocs.com/shipman/canvas.html
        # https://tkdocs.com/shipman/create_oval.html
        self.create_oval(4, 4, 20, 20, fill = "white", tags="oval")
        self.bind("<Button-1>", self.clicked)
    def clicked(self, event): # red 또는 yellow 돌 놓기.
        nextcolor = "red" if self.color != "red" else "yellow"
        self.setColor(nextcolor)
    def setColor(self, color):
        self.delete("oval") # https://pythonguides.com/python-tkinter-canvas/
        self.color = color
        self.create_oval(4, 4, 20, 20, fill = self.color, tags="oval")

window = Tk() # Create a window
window.title("Connect Four") # Set title
frame1 = Frame(window)
frame1.pack()

frame2 = Frame(window)
frame2.pack()

Button = Button(frame2, width = 10, height = 1)

cells = [[Cell(frame1, i, j, width = 20, height = 20).grid(row = i, column = j) for i in range(0, 6)] for j in range(0, 7)]

Button.grid(row = 0, column=0)
window.mainloop() # Create an event loop


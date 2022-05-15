from tkinter import *

_MAXROW = 6
_MAXCOL = 7

Turn = "yellow"
texts = '새로 시작'
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
    def __getColor__(self):
        return self.color
        
    def __checkDiag1(self):
         front = 0
         back = 0
         for i in range(self.col-1, -1, -1):
             if cells[self.row][i].color == self.color:
                 front = front + 1
             else:
                 break
         for i in range(self.col+1, 7):
             if cells[self.row][i].color == self.color:
                 back = back + 1
             else:
                 break    
         if front + back == 3:
             return True
         else:
             return False   
        
                #if cells[row][col] == Turn and cells[row][col + 1] == Turn and cells[row][col + 2] == Turn and cells[row][col+ 3] == Turn:
                #    return True
        
           
    def clicked(self, event): # red 또는 yellow 돌 놓기.
        #nextcolor = "red" if self.color != "red" else "yellow"
        global Turn
        if self.color != "white":
            return
        Turn = "red" if Turn != "red" else "yellow"
        self.setColor(Turn)
        #c = 0
       
       # for i in range(_MAXROW):
       #     for g in range(_MAXCOL):
       #         c = c+1
       #         print(c, cells[i][g].color)
        if self.__checkDiag1():
            print("승리")
        
        
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


Button = Button(frame2, width = 10, height = 1, text = texts)

cells = []
for i in range(_MAXROW):
        cells_col = []
        for j in range(_MAXCOL):
            cell = Cell(frame1, i, j, width=20, height=20)
            cells_col.append(cell)
            cell.grid(row=i, column=j)

        cells.append(cells_col)


Button.grid(row = 0, column=0)
window.mainloop() # Create an event loop


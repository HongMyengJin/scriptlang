from tkinter import *


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
    def Check_Win(self):
        global cells
        #좌우 4개
        row = self.row
        col = self.col
        Same = 0
        value = 1
        #행
        for i in range(-1, 2, 2):
            col = self.col
            row = self.row
            while   col + i > 0 and col + i <= 6 :
                col = col + i
                if cells[self.row][self.col].color == cells[row][col].color:
                    Same = Same + 1
                else:
                    break
        # print(Same)
        # Same = 0 
        #열
        for i in range(-1, 2, 2):
            row = self.row
            col = self.col
            while   row + i > 0 and row + i <= 5 :
                row = row + i
                if cells[self.row][self.col].color == cells[row][col].color:
                    Same = Same + 1
                else:
                    break
        # print(Same)
        # Same = 0
        #정대각선 
        # x: 1, y: -1
        # x: -1, y: 1

        # x: -1, y: -1
        # x: 1, y: 1
        #대각선 x: 
        Same = 0
        for i in range(-1, 2, 2): 
            row = self.row
            col = self.col
            while   row + i >= 0 and row + i <= 5 and col + i >= 0 and col + i <= 6:
                row = row + i
                col = col + i
                if cells[self.row][self.col].color == cells[row][col].color:
                    Same = Same + 1
                else:
                    break
        
        print("반대 대각선: ", Same)
        Same = 0

        for i in range(-1, 2, 2): 
            row = self.row
            col = self.col
            while   row + i >= 0 and row + i <= 5 and col - i >= 0 and col - i <= 6:
                row = row + i
                col = col - i
                if cells[self.row][self.col].color == cells[row][col].color:
                    Same = Same + 1
                else:
                    break
        print("정 대각선: ", Same)
        Same = 0

        print('\n')
        return False
    def clicked(self, event): # red 또는 yellow 돌 놓기.
        global Turn
        #nextcolor = "red" if self.color != "red" else "yellow"

        if self.color != "white":
            return
            
        Turn = "red" if Turn != "red" else "yellow"
        self.setColor(Turn)
        self.Check_Win()
    def setColor(self, color):
        self.delete("oval") # https://pythonguides.com/python-tkinter-canvas/
        self.color = color
        self.create_oval(4, 4, 20, 20, fill = self.color, tags="oval")
    
        

MAXROW = 6
MAXCOL = 7

window = Tk() # Create a window
window.title("Connect Four") # Set title
frame1 = Frame(window)
frame1.pack()
#cells = [[Cell(frame1, i, j, width = 20, height = 20).grid(row = i, column = j) for i in range(0, 7)] for j in range(0, 7)]

cells = []
for i in range(6):
        cells_col = []
        for j in range(7):
            # cell = j
            cell = Cell(frame1, i, j, width=20, height=20)
            cells_col.append(cell)
            cell.grid(row=i, column=j)
        cells.append(cells_col)

frame2 = Frame(window)
frame2.pack()


process_button = Button(frame2, width = 10, height = 1, text = texts)

process_button.grid(row = 0, column=0)
window.mainloop() # Create an event loop


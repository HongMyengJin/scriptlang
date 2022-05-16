from tkinter import *

def Button_Click(event):
    global texts
    global cells
    global Gaming
    global process_button
    global Turn
    if Gaming == False and texts != "새로시작":
        Gaming = True
        texts = "새로시작"
        Turn = "yellow"
        process_button = Button(frame2, width = 10, height = 1, text = texts)
        process_button.grid(row = 0, column=0)
        process_button.bind("<Button-1>", Button_Click) 
    elif Gaming == True and texts == "새로시작":
        cells = []
        for i in range(6):
                cells_col = []
                for j in range(7):
                    # cell = j
                    cell = Cell(frame1, i, j, width=20, height=20)
                    cells_col.append(cell)
                    cell.grid(row=i, column=j)
                cells.append(cells_col)


Turn = "yellow"
texts = "새로시작"
Gaming = True
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
        global Gaming
        #좌우 4개
        row = self.row
        col = self.col
        Same = 0
        value = 1
        
        checkList = [] # 행 * 열 크기 +  열 크기

        #열
        for i in range(-1, 2, 2):
            col = self.col
            row = self.row
            while   col + i > 0 and col + i <= 6 :
                col = col + i
                if cells[self.row][self.col].color == cells[row][col].color:
                    Same = Same + 1
                    checkList.append(row * 7 + col)
                else:
                    break
        if  Same >= 3:
            for i in range(0, len(checkList)):
                cells[checkList[i] // 7][checkList[i] % 7].configure(bg = self.color)
            cells[self.row][self.col].configure(bg = self.color)
            return True

        #행
        checkList = []
        Same = 0
        for i in range(-1, 2, 2):
            row = self.row
            col = self.col
            while   row + i > 0 and row + i <= 5 :
                row = row + i
                if cells[self.row][self.col].color == cells[row][col].color:
                    Same = Same + 1
                    checkList.append(row * 7 + col)
                else:
                    break

        if  Same >= 3:
            for i in range(0, len(checkList)):
                cells[checkList[i] // 7][checkList[i] % 7].configure(bg = self.color)
            cells[self.row][self.col].configure(bg = self.color)
            return True

        checkList = []
        Same = 0
        for i in range(-1, 2, 2): 
            row = self.row
            col = self.col
            while   row + i >= 0 and row + i <= 5 and col + i >= 0 and col + i <= 6:
                row = row + i
                col = col + i
                if cells[self.row][self.col].color == cells[row][col].color:
                    Same = Same + 1
                    checkList.append(row * 7 + col)
                else:
                    break

        if  Same >= 3:
            for i in range(0, len(checkList)):
                cells[checkList[i] // 7][checkList[i] % 7].configure(bg = self.color)
            cells[self.row][self.col].configure(bg = self.color)
            return True

        checkList = []
        Same = 0
        for i in range(-1, 2, 2): 
            row = self.row
            col = self.col
            while   row + i >= 0 and row + i <= 5 and col - i >= 0 and col - i <= 6:
                row = row + i
                col = col - i
                if cells[self.row][self.col].color == cells[row][col].color:
                    Same = Same + 1
                    checkList.append(row * 7 + col)
                else:
                    break

        if  Same >= 3:
            for i in range(0, len(checkList)):
                cells[checkList[i] // 7][checkList[i] % 7].configure(bg = self.color)
            cells[self.row][self.col].configure(bg = self.color)
            return True


        print('\n')
        return False

    def Check_Tie(self):
        global cells
        for i in range(0, 6):
            for j in range(0, 7):
                if cells[i][j].color == "white":
                    return False
        return True
    def clicked(self, event): # red 또는 yellow 돌 놓기.
        global Gaming
        global Turn
        global process_button
        global texts
        #nextcolor = "red" if self.color != "red" else "yellow"
        if Gaming == False:
            return
        if self.color != "white":
            return
            
        Turn = "red" if Turn != "red" else "yellow"
        self.setColor(Turn)
        if  self.Check_Win():
           texts = self.color + " 승리!!"
           process_button = Button(frame2, width = 10, height = 1, text = texts)
           #process_button.text.set(texts)
           process_button.grid(row = 0, column=0)
           process_button.bind("<Button-1>", Button_Click) 
           Gaming = False
        elif self.Check_Tie():
           texts = " 비김!!"
           process_button = Button(frame2, width = 10, height = 1, text = texts)
           #process_button.text.set(texts)
           process_button.grid(row = 0, column=0)
           process_button.bind("<Button-1>", Button_Click) 
           Gaming = False
        

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


process_button = Button(frame2, width = 10, height = 1, text = "새로 시작")
process_button.bind("<Button-1>", Button_Click) 

process_button.grid(row = 0, column=0)
window.mainloop() # Create an event loop


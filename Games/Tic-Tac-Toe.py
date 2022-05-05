from doctest import ELLIPSIS_MARKER
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox

currentToken = 0

def click(event):
    print("클릭위치", event.x, event.y)

class cell(Label):
    global img
    global root
    global cells
    
    def flip(self, event): # 누가 뒤집었지? 
        global currentToken
        
        row = (self.num) // 3
        column = (self.num) % 3

        if  cells[row][column].token != '':
            return False # 이미 뒤집은 패
        if  currentToken % 2 == 0:
            #self.token = 'O'
            cells[row][column].token = 'O'
            print("row: ", row, "column", column)
        else:
            #self.token = 'X'
            cells[row][column].token = 'X'
            print("row: ", row, "column", column)

        if  cells[row][column].token == 'O':
            self.imgLabel = Label(root, image = img[1])
        elif  cells[row][column].token == 'X':
            self.imgLabel = Label(root, image = img[2])
        
        currentToken = currentToken + 1

        for i in range(0, 3):
            for j in range(0, 3):
                cells[i][j].Render()
        if True == cell.Win(self):
            print("이김!!!!!!!!!")
        
    def __init__(self, num):
        self.token = ''
        self.num = int(num)
        self.imgLabel = Label(root, image = img[0])
        super().__init__(root, padx=14, pady=7.2)
        super().bind("<Button-1>", self.flip)
        super().place(width=14,height=7.2)
    def GetToken(self):
        return self.token
    def Win(self):
        row = (self.num) // 3
        column = (self.num) % 3

        # 갯수를 세준다.
        # 첫번째꺼 저장 뒤에 2개 같으면

        # 행, 열
        for i in range(0, 3):
            if  cells[row][column].token != cells[i][column].token:
                break
        else:
            return True # 3개 이상
        for i in range(0, 3):
            if cells[row][column].token != cells[row][i].token:
                break 
        else:
            return True # 3개 이상


        # 대각선
        if  (row == column): # 대각선 검사를 할지 결정   # 행, 열이 같다    
            for i in range(1, 3):
                if cells[i][i].token != cells[0][0].token:
                    break
            else:
                return True
        elif (abs(row - column) == 2): #행과 열의 차 = 2     
            if (cells[0][2].token == cells[1][1].token == cells[2][0].token):
                return True


        return False
    
    def Render(self):
        self.imgLabel.grid(row= (int)(self.num / 3), column= (int)(self.num % 3))
        super().grid(row = self.num // 3, column = self.num % 3)



        
        #해당 행, 열만 체크 => 있으면 True
         
        #대각선 => 없으면 False

root = Tk()
root.title('tic-tac-toe')      
img = [PhotoImage(file = "empty.gif"), PhotoImage(file = "o.gif"), PhotoImage(file = "x.gif")]

#cells = [cell(i) for i in range(0,9)]

cells = [[cell(i * 3 + j) for i in range(0, 3)] for j in range(0, 3)]


for i in range(0, 3):
    for j in range(0, 3):
        cells[i][j].Render()

imgLabel = [Label(root, image = img[0]) for i in range(1, 10)]


frameTitle = Frame(root, padx=120, pady=120)
Label(frameTitle).grid(row=0, column=0)


frame= Frame(root, padx=10, pady=10)
Label(frame).grid(row=0, column=0)
 

# for i in range(0, 3):
#      for j in range(0, 3):
#         cells[i][j].bind("<Button-1>") 

# a = input("행과 열을 입력하세요.").split()

# # #행
# # a[0] 
# # #열
# # a[1]

#cells[0][0].flip('O')


 

 #왼쪽 마우스 버튼 바인딩

root.mainloop()

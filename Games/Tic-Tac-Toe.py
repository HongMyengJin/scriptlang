from doctest import ELLIPSIS_MARKER
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox

currentToken = 0

class cell(Label):
    global img
    global root
    global cells
    def __init__(self, num):
        self.token = ''
        self.num = num
        imgLabel = Label(root, image = img[0])

    def Win(self):
        row = self.num / 3
        column = self.num % 3

        # 갯수를 세준다.
        # 첫번째꺼 저장 뒤에 2개 같으면

        # 행, 열
        for j in range(0, 2):
            for i in range(0, 3):
                if j == 0:
                    if cells[row][column].token != cells[i][column].token:
                        break
                else:
                       if cells[row][column].token != cells[row][i].token:
                        break
            else:
                return True # 3개 이상

        # 대각선
        if  (row == column) | (abs(row - column) == 2): # 대각선 검사를 할지 결정   # 행, 열이 같거나 행과 열의 차 = 2         
            for i in range(1, 3):
                if cells[i][i].token != cells[0][0]:
                    break
            else:
                return True

            if (cells[0][2] == cells[1][1] == cells[2][0]):
                return True

            return False

    def flip(self, event): # 누가 뒤집었지? 
        if  self.token != '':
            return False # 이미 뒤집은 패
        self.token = event
        if    self.token == 'O':
            imgLabel = Label(root, image = img[1])
        elif  self.token == 'X':
            imgLabel = Label(root, image = img[2])
        
        return  cell.Win()# 새로 등록된 패 #혹시 모르니까 오류뜨면 여기일듯
        
    

    


        
        #해당 행, 열만 체크 => 있으면 True
         
        #대각선 => 없으면 False

         



    # def flip(self, event):

cells = [cell() for i in range(1,10)]


img = [PhotoImage(file = "empty.gif"), PhotoImage(file = "o.gif"), PhotoImage(file = "x.gif")]

root = Tk()
root.title('tec-tac-toe')

#frameTitle = Frame(root, padx=120, pady=120)

#frameTitle.grid(row=2, column=2) #, sticky='w'
#Label(frameTitle).grid(row=0, column=0)



imgLabel = [Label(root, image = img[2]) for i in range(1, 10)]


        
# imgLabel1 = Label(root, image = img[1])
# imgLabel2 = Label(root, image = img[1])
# imgLabel3 = Label(root, image = img[1])
# imgLabel1.grid(row = 0, column = 0)
# imgLabel2.grid(row = 0, column = 1)
# imgLabel3.grid(row = 0, column = 2)

imgLabel[0] = Label(root, image = img[0])
t = 0
for j in range (0, 3):
    for i in range(0, 3):
        imgLabel[t].grid(row= i, column=j)
        t = t + 1

# frameCombo = Frame(root, padx=10, pady=10)
# frameCombo.grid(row=1, column=0, sticky='news') 
# combo_str = ['수퍼수프림', '감자피자', '고구마피자'] 
# combo = ttk.Combobox(frameCombo, values=combo_str) 
# combo.pack(side=LEFT, expand=True, fill='both') 
# combo.set('피자 선택')

# frameCheckbox = Frame(root, padx=10, pady=10)
# frameCheckbox.grid(row=2, column=0) 
# chkValue = [] 
# strCheck = ['치즈 추가', '피클 추가', '콜라 추가']
# for i, s in enumerate(strCheck): chkValue.append(IntVar()) # Variable 클래스: get(), set() 함수 사용
# ttk.Checkbutton(frameCheckbox, text=s, variable=chkValue[i]).grid(row = 0, column=i)
# frameButtons = Frame(root, padx=10, pady=10, bg='#a0a0a0')
# frameButtons.grid(row=3, column=0, sticky='news')
# Button(frameButtons, command=onOK, text='확인').pack(side=LEFT, expand=True, fill='both')
# Button(frameButtons, command=onCancel, text='취소').pack(side=RIGHT, expand=True, fill='both') 

frameTitle = Frame(root, padx=120, pady=120)
Label(frameTitle).grid(row=0, column=0)



root.mainloop()
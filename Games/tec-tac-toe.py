from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox

currentToken = 0

class cell(Label):

    def __init__(self):
        self.token = ''

    # def flip(self, event):

cells = [cell() for i in range(1,10)]




root = Tk()
root.title('tec-tac-toe')

#frameTitle = Frame(root, padx=120, pady=120)

#frameTitle.grid(row=2, column=2) #, sticky='w'
#Label(frameTitle).grid(row=0, column=0)

img = [PhotoImage(file = "o.gif"), PhotoImage(file = "x.gif"), PhotoImage(file = "empty.gif")]


imgLabel = [Label(root, image = img[2]) for i in range(1, 10)]


        
# imgLabel1 = Label(root, image = img[1])
# imgLabel2 = Label(root, image = img[1])
# imgLabel3 = Label(root, image = img[1])
# imgLabel1.grid(row = 0, column = 0)
# imgLabel2.grid(row = 0, column = 1)
# imgLabel3.grid(row = 0, column = 2)

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
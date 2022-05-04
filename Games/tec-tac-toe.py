from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox

currentToken = 0

class cell(Label):

    def __init__(self):
        self.flipvalue = False

    def test(self):
        self.flipvalue = True

    def FlipValueReturn(self):
        return self.flipvalue

def onOK(): # “확인”버튼핸들러
    global chkValue, strCheck
    for i, v in enumerate(chkValue):
        if v.get() == 1: # Variable 클래스: get()함수 사용
            print(strCheck[i], "선택됨") 
    messagebox.showinfo(title='알림', message='피자가 선택되었습니다')
    root.destroy()

def onCancel(): # “취소”버튼핸들러
    messagebox.showinfo(title='알림', message='피자 선택이 취소되었습니다')
    root.destroy()


Cells = [cell() for i in range(1,10)]

for i in range(0, 5):
    Cells[i].test()

for i in range(0, 9):
    print(Cells[i].FlipValueReturn())





root = Tk()
root.title('tec-tac-toe')

frameTitle = Frame(root, padx=120, pady=120)

frameTitle.grid(row=0, column=0, sticky='w')
Label(frameTitle).grid(row=0, column=0)

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
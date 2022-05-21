from asyncio.base_futures import _FINISHED
import math
import random
from tkinter import * # Import tkinter
    
class Hangman:
    global hiddenWord
    global guessWord
    global nMissedLetters
    global nMissChar
    global finished
    global words
    global canvas
    global texts
    global textlist
    global miss
    
    def __init__(self):
        self.draw()
        
    def setWord(self):
        hiddenword = random.choice(words)
        hiddenword = list(hiddenword)
        print(hiddenword)
        guessword = ['*']*len(hiddenword)
        nMissChar = 0
        nCorrectChar = 0
        nMissedLetters = []
        textlist = ' '
        textlist = texts + ''.join(guessword)
        canvasname = canvas.create_text(200,190,text=textlist)

        miss = canvas.create_text(200,200,text='')
        self.draw()

    def draw(self):
        global canvasname
        global miss
        # 한꺼번에 지울 요소들을 "hangman" tag로 묶어뒀다가 일괄 삭제.
        canvas.delete("hangman")
        
        # 인자 : (x1,y1)=topleft, (x2,y2)=bottomright, start=오른쪽이 0도(반시계방향), extent=start부터 몇도까지인지
        #    style='pieslice'|'chord'|'arc'
        canvas.create_arc(20, 200, 100, 240, start = 0, extent = 180, style='chord', tags = "hangman") # Draw the base
        canvas.create_line(60, 200, 60, 20, tags = "hangman")  # Draw the pole
        canvas.create_line(60, 20, 160, 20, tags = "hangman") # Draw the hanger 
        radius = 20 # 반지름
        
        if 0 < nMissChar:   #위에 그리기
            canvas.create_line(160, 20, 160, 40, tags = "hangman") # Draw the hanger
 
        if 1 < nMissChar:   #머리
        # Draw the circle
            canvas.create_oval(140, 40, 180, 80, tags = "hangman") # Draw the hanger

        if 2 < nMissChar:   #왼쪽 팔
        # Draw the left arm (중심(160,60)에서 45도 움직인 지점의 x좌표는 cos로, y좌표는 sin으로 얻기)
            x1 = 160 - radius * math.cos(math.radians(45))
            y1 = 60 + radius * math.sin(math.radians(45))
            x2 = 160 - (radius+60) * math.cos(math.radians(45))
            y2 = 60 + (radius+60) * math.sin(math.radians(45))
            canvas.create_line(x1, y1, x2, y2, tags = "hangman")

        if 3 < nMissChar:   #오른쪽 팔
            x11 = 160 + radius * math.cos(math.radians(45))
            y11 = 60 + radius * math.sin(math.radians(45))
            x22 = 160 + (radius+60) * math.cos(math.radians(45))
            y22 = 60 + (radius+60) * math.sin(math.radians(45))
            canvas.create_line(x11, y11, x22, y22, tags = "hangman")
        
        if 4 < nMissChar:   #몸통
            canvas.create_line(160, 80, 160, 140, tags = "hangman") # Draw the hanger 
        
        if 5 < nMissChar:   #왼쪽다리
            x3 = 160 
            y3 = 140 
            x4 = 160 + 60 * math.cos(math.radians(45))
            y4 = 140 + 60 * math.cos(math.radians(45))
            canvas.create_line(x3, y3, x4, y4, tags = "hangman")

        if 6 < nMissChar:   #오른쪽다리
            x33 = 160 
            y33 = 140 
            x44 = 160 - 60 * math.cos(math.radians(45))
            y44 = 140 + 60 * math.cos(math.radians(45))
            canvas.create_line(x33, y33, x44, y44, tags = "hangman")
        
            
# Initialize words, get the words from a file
infile = open("hangman.txt", "r")
words = infile.read().split()  
    
window = Tk() # Create a window
window.title("행맨") # Set a title
    
width = 400
height = 280    
# 선, 다각형, 원등을 그리기 위한 캔버스를 생성
canvas = Canvas(window, bg = "white", width = width, height = height)
canvas.pack()


hiddenword = random.choice(words)
hiddenword = list(hiddenword)

print(hiddenword)
guessword = ['*']*len(hiddenword)
nMissChar = 0
nCorrectChar = 0
nMissedLetters = []
texts = "단어 추측 : "
textlist = ' '


textlist = texts + ''.join(guessword)
canvasname = canvas.create_text(200,190,text=textlist)

miss = canvas.create_text(200,200,text='')

def processKeyEvent(event):  
    global nCorrectChar
    global nMissChar
    #global hangman
    if event.char >= 'a' and event.char <= 'z':
            check =0
            for i in range(0,len(hiddenword)):
                if event.char == hiddenword[i]:
                    check = 1
                    nCorrectChar = nCorrectChar+ 1
                    print(guessword)
                    guessword[i] = hiddenword[i]
                    print(guessword)
                    textlist = texts + ''.join(guessword)
                    canvas.itemconfig(canvasname,text=textlist)
                    if nCorrectChar == len(hiddenword):
                         canvas.itemconfig(miss,text="계속하려면 Enter를 누르세요")
                         
            if check == 0:
                nMissedLetters.append(event.char)
                nMissChar = nMissChar  + 1 
                print(nMissedLetters)
                canvas.itemconfig(miss,text=nMissedLetters)
                if nMissChar == 7:
                    canvas.itemconfig(canvasname,text=hiddenword)
                    canvas.itemconfig(miss,text="계속하려면 Enter를 누르세요") 
                    
                    
            hangman.draw()     
                    
    elif event.keycode == 13:
            hangman.setWord()
            

hangman = Hangman()
# Bind with <Key> event
canvas.bind("<Key>", processKeyEvent)
# key 입력 받기 위해 canvas가 focus 가지도록 함.
canvas.focus_set()
window.mainloop() # Create an event loop

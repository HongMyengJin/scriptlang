from asyncio.base_futures import _FINISHED
import math
import random
from tkinter import * # Import tkinter
    
class Hangman:
    global hiddenWord
    global guessWord
    global nCorrectChar
    global nMissChar
    global nNissedLetters
    global finished
    global words
    global canvas

    
    def __init__(self):
        self.draw()
        
    def setWord(self):
        pass
        
    

    def draw(self):
        global canvasname
        # 한꺼번에 지울 요소들을 "hangman" tag로 묶어뒀다가 일괄 삭제.
        canvas.delete("hangman")
        
        canvasname = canvas.create_text(200,190,text=guessword)

        # 인자 : (x1,y1)=topleft, (x2,y2)=bottomright, start=오른쪽이 0도(반시계방향), extent=start부터 몇도까지인지
        #    style='pieslice'|'chord'|'arc'
        canvas.create_arc(20, 200, 100, 240, start = 0, extent = 180, style='chord', tags = "hangman") # Draw the base
        canvas.create_line(60, 200, 60, 20, tags = "hangman")  # Draw the pole
        canvas.create_line(60, 20, 160, 20, tags = "hangman") # Draw the hanger 
        radius = 20 # 반지름
        canvas.create_line(160, 20, 160, 40, tags = "hangman") # Draw the hanger

        # Draw the circle
        canvas.create_oval(140, 40, 180, 80, tags = "hangman") # Draw the hanger

        # Draw the left arm (중심(160,60)에서 45도 움직인 지점의 x좌표는 cos로, y좌표는 sin으로 얻기)
        x1 = 160 - radius * math.cos(math.radians(45))
        y1 = 60 + radius * math.sin(math.radians(45))
        x2 = 160 - (radius+60) * math.cos(math.radians(45))
        y2 = 60 + (radius+60) * math.sin(math.radians(45))
        canvas.create_line(x1, y1, x2, y2, tags = "hangman")

        x11 = 230 - radius * math.cos(math.radians(45))
        y11 = 60 + (radius+60) * math.sin(math.radians(45))
        x22 = 230 - (radius+60) * math.cos(math.radians(45))
        y22 = 60 + radius * math.sin(math.radians(45))
        canvas.create_line(x11, y11, x22, y22, tags = "hangman")
        
        canvas.create_line(160, 80, 160, 140, tags = "hangman") # Draw the hanger 
        
        x3 = 160 
        y3 = 140 
        x4 = 120 -(radius) * math.cos(math.radians(45))
        y4 = 180 +(radius) * math.cos(math.radians(45))
        canvas.create_line(x3, y3, x4, y4, tags = "hangman")

        x33 = 230 - 1 * math.cos(math.radians(45))
        y33 = 140 + 1* math.sin(math.radians(45))
        x44 = 230 - 1* math.cos(math.radians(45))
        y44 = 140 + 1 * math.sin(math.radians(45))
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
nMissChar = []
nCorrectChar = 0


def processKeyEvent(event):  
        if event.char >= 'a' and event.char <= 'z':
            for i in range(0,len(hiddenword)):
                if event.char == hiddenword[i]:
                    print(guessword)
                    guessword[i] = hiddenword[i]
                    print(guessword)
                    canvas.itemconfig(canvasname,text = guessword)
        elif event.keycode == 13:
            pass
            

hangman = Hangman()
# Bind with <Key> event
canvas.bind("<Key>", processKeyEvent)
# key 입력 받기 위해 canvas가 focus 가지도록 함.
canvas.focus_set()
window.mainloop() # Create an event loop

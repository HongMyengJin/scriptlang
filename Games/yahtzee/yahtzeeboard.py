from tkinter import *
from tkinter import font
import tkinter
from player import *
from dice import *
from configuration import *
from tkinter import messagebox

class YahtzeeBoard:
    # index들.
    UPPERTOTAL = 6  # "Upper Scores" 위치의 index.
    UPPERBONUS = 7  # "Upper Bonus(35)" 위치의 index.
    LOWERTOTAL = 15  # "Lower Scores" 위치의 index.
    TOTAL = 16  # "Total" 위치의 index.

    #주사위굴렸는지 확인
    checkDice = 0

    # 객체 리스트
    dice = []       # Dice() 객체의 리스트.
    diceButtons = [] # 각 주사위를 표현하는 Button 객체의 리스트.
    fields = []     # 각 플레이어별 점수판(카테고리). Button 객체의 2차원 리스트.
                    # 열: 플레이어 (0열=플레이어1, 1열=플레이어2,…)
                    # 17행: upper카테고리6행, upperScore, upperBonus, lower카테고리7행, LowerScore, Total
    players = []    # 플레이어 수 만큼의 Player 인스턴스를 가짐.
    numPlayers = 0  # # 플레이어 수
    player = 0      # players 리스트에서 현재 플레이어의 index.
    round = 0       # 13 라운드 중 몇번째인지 (0~12 사이의 값을 가짐)
    roll = 0        # 각 라운드에서 3번 중 몇번째 굴리기인지 (0~2 사이의 값을 가짐)
    # 색깔
    color_btn_bg = 'SystemButtonFace'

    def __init__(self):
        self.InitGame()

    def InitGame(self):     #player window 생성하고 최대 10명까지 플레이어 설정
        self.pwindow = Tk()
        self.window_Close = ()
        self.TempFont = font.Font(size=12, weight='bold', family='Consolas')
        self.label = []
        self.entry = []
        self.label.append( Label(self.pwindow, text='플레이어 수', font=self.TempFont ) )
        self.label[0].grid(row=0, column=0)

        for i in range(1,11):
            self.label.append( Label(self.pwindow, text='플레이어'+str(i)+' 이름', font=self.TempFont))
            self.label[i].grid(row=i, column=0)
        for i in range(11):
            self.entry.append(Entry(self.pwindow, font=self.TempFont))
            self.entry[i].grid(row=i, column=1)
        Button(self.pwindow, text='Yahtzee 플레이어 설정 완료', font=self.TempFont, command=self.InitAllPlayers).grid(row=11, column=0)

        self.pwindow.mainloop()

    def InitAllPlayers(self):
        '''
        [플레이어 설정 완료 버튼 누르면 실행되는 함수]
        numPlayers를 결정하고 이 숫자에 따라 각 player에게 필요한 정보들을 초기화.
        기존 toplebel 윈도우를 닫고 Yahtzee 보드 윈도우 생성.
        '''
        self.numPlayers = int(self.entry[0].get())
        for i in range(1, self.numPlayers+1):
            self.players.append(Player(str(self.entry[i].get())))

        ##################################################       
        # Yahtzee 보드판: 플레이어 수 만큼 생성
        
        self.window = Tk('Yahtzee Game')
        self.TempFont = font.Font(size=12, weight='bold', family='Consolas')

        for i in range(5): #Dice 객체 5개 생성
            self.dice.append(Dice())

        self.rollDice = Button(self.window, text='Roll Dice', font=self.TempFont, command=self.rollDiceListener, bg=self.color_btn_bg)  # Roll Dice 버튼
        self.rollDice.grid(row=0, column=0)
        for i in range(5):  #dice 버튼 5개 생성
	        #각각의 dice 버튼에 대한 이벤트 처리 diceListener 연결
            #람다 함수를 이용하여 diceListener 매개변수 설정하면 하나의 Listener로 해결
            self.diceButtons.append(Button(self.window, text='?', font=self.TempFont, width=8, bg=self.color_btn_bg, command=lambda row=i: self.diceListener(row))) 
            self.diceButtons[i].grid(row=i + 1, column=0)
        
        for i in range(self.TOTAL + 2):  # i행 : 점수
            Label(self.window, text=Configuration.configs[i], font=self.TempFont).grid(row=i, column=1)
            for j in range(self.numPlayers):  # j열 : 플레이어
                if (i == 0):  # 플레이어 이름 표시
                    Label(self.window, text=self.players[j].toName(), font=self.TempFont).grid(row=i, column=2 + j)
                else:
                    if (j==0): #각 행마다 한번씩 리스트 추가, 다중 플레이어 지원
                        self.fields.append(list())
                    #i-1행에 플레이어 개수 만큼 버튼 추가하고 이벤트 Listener 설정, 매개변수 설정
                    self.fields[i-1].append(Button(self.window, text="", font=self.TempFont, width=8,
                        command=lambda row=i-1: self.categoryListener(row)))
                    self.fields[i-1][j].grid(row=i,column=2 + j)
                    # 누를 필요없는 버튼은 disable 시킴
                    if (j != self.player or (i-1) == self.UPPERTOTAL or (i-1) == self.UPPERBONUS 
                        or (i-1) == self.LOWERTOTAL or (i-1) == self.TOTAL):
                        self.fields[i-1][j]['state'] = 'disabled'
                        self.fields[i-1][j]['bg'] = 'light gray'
        
        #상태 메시지 출력
        self.bottomLabel=Label(self.window, text=self.players[self.player].toName()+
            "차례: Roll Dice 버튼을 누르세요", width=35, font=self.TempFont)
        self.bottomLabel.grid(row=self.TOTAL + 2, column=0, columnspan=2)
        self.window.mainloop()

    # 주사위 굴리기 함수.
    def rollDiceListener(self):
        # 'state' 값이 'disabled'가 아닌 모든 주사위 값을 새로 할당하고 화면에 표시.
        # TODO: 구현
        for i in range(5):
            if(self.diceButtons[i]['state'] != 'disabled'):
                self.checkDice = 1
                self.dice[i].rollDie()
                self.diceButtons[i].configure(text=str(self.dice[i].getRoll()))

        # self.roll 이 0, 1 일 때 : 
        if (self.roll == 0 or self.roll ==1):
            self.roll += 1
            self.rollDice.configure(text="Roll Again")
            self.bottomLabel.configure(text="보관할 주사위 선택 후 Roll Again")
        elif (self.roll==2):
            self.bottomLabel.configure(text="카테고리를 선택하세요")
            self.rollDice['state'] = 'disabled'
            self.rollDice['bg'] = 'light gray'
            self.roll = 0

    # 각 주사위에 해당되는 버튼 클릭 : disable 시키고 배경색을 어둡게 바꿔 표현해 주기.
    def diceListener(self, row):
        if self.checkDice != 1:
            return
        if not(self.diceButtons[row]['bg'] == 'light gray' and self.diceButtons[row]['state'] == 'disabled'):
            self.diceButtons[row]['state'] = 'disabled'
            self.diceButtons[row]['bg'] = 'light gray'


    # 카레고리 버튼 눌렀을 때의 처리.
    #   row: 0~5, 8~14
    def Restart(self):
        global dice
        global diceButtons
        global fields
        global players
        global numPlayers
        global player
        global round
        global roll
        #diceButtons = [] # 각 주사위를 표현하는 Button 객체의 리스트.
        fields = []     # 각 플레이어별 점수판(카테고리). Button 객체의 2차원 리스트.
                        # 열: 플레이어 (0열=플레이어1, 1열=플레이어2,…)
                        # 17행: upper카테고리6행, upperScore, upperBonus, lower카테고리7행, LowerScore, Total
        players = []    # 플레이어 수 만큼의 Player 인스턴스를 가짐.
        numPlayers = 0  # # 플레이어 수
        player = 0      # players 리스트에서 현재 플레이어의 index.
        round = 0       # 13 라운드 중 몇번째인지 (0~12 사이의 값을 가짐)
        roll = 0        # 각 라운드에서 3번 중 몇번째 굴리기인지 (0~2 사이의 값을 가짐)
        self.players = []
        self.dice = []
        self.fields = []
        self.entry = []
        self.round = 0
        self.diceButtons = []
        self.fields = []
        self.player = 0
        #self.rollDice = []
        self.pwindow.destroy()
        self.window.destroy()
        self.window_Close.destroy()
        self.InitGame()
    def categoryListener(self, row):
        self.roll = 0
        if self.checkDice != 1:
            return
        score = Configuration.score(row, self.dice)      #점수 계산
        # index : 0~12
        index = row
        if (row>7):
            index = row-2
        cur_player = self.players[self.player]
        # (1) cur_player에 setScore(), setAtUse() 호출하여 점수와 사용상태 반영.
        # (2) 선택한 카테고리의 점수를 버튼에 적고 
        # (3) 버튼을 disable 시킴.
        # TODO: 구현

        cur_player.setScore(score, index)
        cur_player.setAtUse(index)
        self.fields[row][self.player].configure(text=str(score))
        self.fields[row][self.player]['state'] = 'disabled'
        self.fields[row][self.player]['bg'] = 'light gray'
        
        # UPPER category가 전부 사용되었으면(cur_player.allUpperUsed()로써 확인)
        # -> cur_player.getUpper() 점수에 따라
        #    UI의 UPPERTOTAL, UPPERBONUS 에 내용 채우기.
        # TODO: 구현
        if (cur_player.allUpperUse()):
            self.fields[self.UPPERTOTAL][self.player].configure(text=str(cur_player.getUpper()))
        if (cur_player.getUpper() > 63):
            self.fields[self.UPPERBONUS][self.player].configure(text="35")  # UPPERBONUS=7
        else:
            self.fields[self.UPPERBONUS][self.player].configure(text="0")  # UPPERBONUS=7

        # LOWER category 전부 사용되었으면(cur_player.allLowerUse()로써 확인) 
        # -> cur_player.getLower() 점수에 따라
        #   UI의 LOWERTOTAL 에 내용 채우기.
        # TODO: 구현
        if (cur_player.allLowerUse()):
            self.fields[self.LOWERTOTAL][self.player].configure(text=str(cur_player.getLower()))
        # UPPER category와 LOWER category가 전부 사용되었으면 
        # -> UI의 TOTAL 에 내용 채우기.
        # TODO: 구현
        if (cur_player.allUpperUse() and cur_player.allLowerUse()):
            self.fields[self.TOTAL][self.player].configure(text=str(cur_player.getTotal()))
       
        # 다음 플레이어로 가기.
        self.player = (self.player + 1) % self.numPlayers
        cur_player = self.players[self.player]
        self.checkDice = 0

        # 선택할 수 없는 카테고리들과 현재 player 것이 아닌 버튼들은 disable 시키기.
        # 그 외는 enable 시키기.
        # TODO: 구현
        for i in range(self.TOTAL + 1):
            for j in range(self.numPlayers):
                if not self.fields[i][j]['text']:
                    self.fields[i][j]['state'] = 'normal'
                    self.fields[i][j]['bg'] = self.color_btn_bg
                self.fields[i][j].grid(row=i+1, column=2 + j)
 
                if (j != self.player or (i) == self.UPPERTOTAL or (i) == self.UPPERBONUS or (i) == self.LOWERTOTAL or (i) == self.TOTAL):
                        self.fields[i][j]['state'] = 'disabled'
                        self.fields[i][j]['bg'] = 'light gray'

        # 라운드 증가 시키기.
        if self.player == 0:
            self.round += 1

        # 게임이 종료되었는지 검사 (13 round의 마지막 플레이어일 때) 
        # -> 이긴 사람을 알리고 새 게임 시작.
        # TODO: 구현
        if (self.round == 13):
            print(self.round)
            scores = []
            for score in self.fields[self.TOTAL]:
                scores.append(int(score['text']))
            greatest = max(scores)
            print(greatest)
            win_players = ""
            for player in self.players:
                if player.getTotal() is greatest:
                    win_players = player.toName()
            self.window_Close = Tk()
            self.window_Close.geometry("200x100+500+200")
            Label(self.window_Close, text=win_players+"이김!").place(x=100,y=50,anchor='center')
            exit_button = tkinter.Button(self.window_Close, text = "ReStart", command = self.Restart)
            exit_button.pack()
            self.window_Close.mainloop()
            # window.destroy()
            # self.InitGame()
            #window.mainloop()
            return

        # 다시 Roll Dice 버튼과 diceButtons 버튼들을 활성화.
        self.rollDice.configure(text="Roll Dice")
        self.rollDice['state'] = 'normal'
        self.rollDice['bg'] = self.color_btn_bg
        for i in range(5):  #dice 버튼 5개 생성
            self.diceButtons[i].configure(text='')
            self.diceButtons[i]['state'] = 'normal'
            self.diceButtons[i]['bg'] = self.color_btn_bg

        # bottomLabel 초기화.
        self.bottomLabel.configure(text=cur_player.toName()+
            "차례: Roll Dice 버튼을 누르세요")

if __name__ == '__main__':
    YahtzeeBoard()


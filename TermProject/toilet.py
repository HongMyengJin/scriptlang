from msilib.schema import CheckBox, ListBox
from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
import folium
import webbrowser
import folium as g
from tkinter import messagebox as msg
import spam
from enum import Enum


g_Tk = Tk()
g_Tk.geometry("900x600+250+100")

class DataEnum(Enum):
    eName = 0
    eAddress = 1
    eNumber = 2
    eOpenTime = 3
    eLat = 4
    eLon = 5
    eGB_Check = 6
    eB_Closet = 7
    eG_Closet = 8

class G_bClosetEnum(Enum):
    B_Closet = 0
    G_Closet = 1
    All_Closet = 2

Lat = []
Lon = []
IsPublic = []
Name = []
Address = []
Manage = []
Number = []
OpenTime = []
indexData = []
GB_Check = []
G_Closet = []
B_Closet = []

Favori_List = []
GBName_CheckButton = False
              #B  G
ClosetList = [[], []]
#       0       1       2       3          4   5    6           7          8
Data = [Name, Address, Number, OpenTime, Lat, Lon, GB_Check, B_Closet, G_Closet]
Lat_Data = 0.0
Lon_Data = 0.0
Name_Data = ""

text =""
data =""

CurListBox3Index = None
book_Mark = [[],[]]
fontMidium= font.Font(g_Tk, size = 15, family='경기천년제목 Bold')
fontMidium1 = font.Font(g_Tk, size = 13, family='경기천년제목 Bold')
fontMidium2= font.Font(g_Tk, size = 10, family='경기천년제목 Medium')
fontMidium3= font.Font(g_Tk, size = 7, family='경기천년바탕 Bold')
fontMidium4= font.Font(g_Tk, size = 14, family='경기천년바탕 Regular')
fontMidium5= font.Font(g_Tk, size = 13, family='경기천년바탕 Medium')
fontMidium6= font.Font(g_Tk, size = 11, family='경기천년제목 Medium')
class ImageLabel(Label):
    def __init__(self, parent, filenameOrUrl = None, width = 0, height = 0, imageLabel = None):
        super().__init__(parent)
        if width:
            self.width = width
        if height:
            self.height = height
        if filenameOrUrl:
            self.setImage(filenameOrUrl)

    def setImage(self, filenameOrUrl):
        from PIL import Image, ImageTk
        if filenameOrUrl.startswith('http'):
            from io import BytesIO
            import urllib.request
            url = filenameOrUrl
            try:
                with urllib.request.urlopen(url) as u:
                    raw_data = u.read()
            except urllib.error.URLError:
                print('urllib.error.URLError!')
                return
            im = Image.open(BytesIO(raw_data))
        elif filenameOrUrl:
            im= (Image.open(filenameOrUrl))
        im = im.resize((self.width,self.height), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(im)
        self.configure(image = img)
        self.image = img


def InitScreen():
    fontTitle = font.Font(g_Tk, size=22, weight='bold', family='경기천년제목 Bold')
    
    fontNormal = font.Font(g_Tk, size = 15, weight='bold')


    



    frameList = Frame(g_Tk, padx=30, pady=10, bg='#C8E6A8', width= 1550, height= 100)
    frameList.pack(side="bottom", fill="both")

    frameTitle = Frame(g_Tk, padx = 10, pady=10, bg='#C8E6A8')
    frameTitle.pack(fill='x')


    frameEntry = Frame(g_Tk, bg='#C8E6A8', width= 500, height= 200)
    frameEntry.pack(side="top", fill="both", expand= False)


    frameCombo = Frame(g_Tk, pady=20, bg='#C8E6A8', width= 50, height= 50)
    frameCombo.pack(side='top', fill='both', expand= False)
    #페이지 기준 나누기
    style = ttk.Style()
    style.configure("BW.TLabel", foreground="#C8E6A8", background="#C8E6A8")
    notebook= ttk.Notebook(frameEntry, width =250, height = 83, style = "BW.TLabel")
    notebook.pack(side='left')
    global frameNote
    frameNote = Frame(g_Tk)
    notebook.add(frameNote, text="            즐겨찾기            ")
    global frameNote2
    frameNote2 = Frame(g_Tk)
    notebook.add(frameNote2, text="            지도            ")
    #frameCombo.place(x = 50, y = 310)
    frameSearch = Frame(g_Tk, padx = 10, bg='#C8E6A8', width= 550, height= 80)
    frameSearch.pack(side='top',fill = 'both')
    frameCheck = Frame(g_Tk,  padx = 30,bg='#C8E6A8', width= 50, height= 18)

    frameCheck.pack(side='top', fill='both', expand= False)


    #frameCheck.place(x = 250, y = -250)

    #frameCheck.place(x = 675, y = 365)
    
#경기천년제목 Medium

    # MainText = Label(frameTitle, font = fontTitle, text="[공중 화장실 찾기 App]")
    # MainText.pack(anchor="center", fill="both")

    global SearchListBox 
    slist = ["가평군", "고양시", "과천시","광명시", "광주시", "구리시", 
             "군포시", "김포시", "남양주시", "동두천시", "부천시", "수원시", 
             "성남시", "시흥시", "안산시", "안성시", "안양시", "양주시", 
             "양평군", "여주시", "오산시", "용인시", "의왕시", 
             "의정부시", "이천시", "파주시", "포천군", "평택시", "하남시",
             "화성시"] 
    SearchListBox = ttk.Combobox(frameCombo, values = slist)
    SearchListBox.set('시/군 선택')    
    SearchListBox.pack(side='left', padx= 5, expand=False )
    SearchListBox.configure(font=("경기천년제목 Light", 16))
     
    SearchListBox.bind("<<ComboboxSelected>>", ComboChange)
    



    global chkValue
    global CheckButton
    
    global chkBValue
    global CheckBoy
    
    global chkGValue
    global CheckGirl
    
    chkValue = IntVar()
    chkBValue = IntVar()
    chkGValue = IntVar()
    s = ttk.Style()
    s.configure('Green.TCheckbutton', background = '#C8E6A8', foreground = 'white')

    CheckButton = Checkbutton(frameCombo, bg = '#C8E6A8', activebackground= '#C8E6A8', text="공용화장실X", variable=chkValue, font = ("경기천년제목 Light", 11), command = Check_Public).pack(side='left')
    
    
    CheckBoy = Checkbutton(frameCheck, padx = 5, bg = '#C8E6A8', activebackground= '#C8E6A8',  text="남자 개수", font = ("경기천년제목 Light", 11), variable=chkBValue, command = Check_Box_B).pack(side='left', fill  = "y")
    CheckGirl = Checkbutton(frameCheck, padx = 0, bg = '#C8E6A8',activebackground= '#C8E6A8',text="여자 개수", font = ("경기천년제목 Light", 11), variable=chkGValue, command = Check_Box_G).pack(side='left', fill  = "y")
    

    FavoritButton = Button(frameEntry, font=fontMidium2, \
           text='즐겨찾기\n\n추가', command = Favorit_ButtonEvt)
    FavoritButton.pack(side='left', padx= 0, fill = "both")


    SearchButton = Button(frameSearch, font=fontMidium, \
           text='검색', command = Search_Name)
    SearchButton.pack(side='right', padx= 6, expand=False)

    global InputLabel 
    InputLabel = Entry(frameSearch, font = fontMidium, \
            width = 32, borderwidth = 6, relief = 'flat')
    InputLabel.pack(side="right", padx= 10, expand = False)
    global imageLabel
    imageLabel = ImageLabel(frameCombo, width=40, height=35)
    imageLabel.setImage('image/Email_Close.gif')
    imageLabel.bind('<Button-1>', MailButton)
    imageLabel.pack(side = "right", padx= 15)



    imageLabel3 = ImageLabel(frameTitle, width=860, height=150)
    imageLabel3.setImage('image/AppName.png')
    imageLabel3.pack(side = "top", expand = False)

    global InputEmail 
    InputEmail = Entry(frameCombo, font = fontMidium4, \
            width = 42, borderwidth = 8.5, relief = 'flat')
    InputEmail.pack(side="right", padx = 10, expand = False)
    
    global listBox
    LBScrollbar = Scrollbar(frameList)
    listBox = Listbox(frameList, selectmode='extended',\
    font=fontMidium1, width=3, height=8, \
    borderwidth=12, relief='ridge', yscrollcommand=LBScrollbar.set)
    listBox.bind('<<ListboxSelect>>', event_for_listbox)
    listBox.pack(side='left', anchor='n', expand=True, fill="both")
    LBScrollbar.pack(side='left', fill='y')
    LBScrollbar.config(command=listBox.yview)
    
    global listBox2
    listBox2 = Listbox(frameList, selectmode='extended',\
    font=fontMidium2, width=5, height=7, \
    borderwidth=12, background = '#fffecb', relief='flat', yscrollcommand=LBScrollbar.set)
    listBox2.pack(side='left', anchor='n', expand=True, fill="both")

    global listBox3
    LBScrollbar = Scrollbar(frameNote)
    listBox3 = Listbox(frameNote, selectmode='extended',\
    font=fontMidium2, width=5, height=7, \
    borderwidth=12, background = '#bdecb6', relief='flat', yscrollcommand=LBScrollbar.set)
    listBox3.bind('<<ListboxSelect>>', Book_MarkListClick)
    listBox3.pack(side='left', anchor='n', expand=True, fill="both")
    LBScrollbar.pack(side='left', fill='y')
    LBScrollbar.config(command=listBox3.yview)

    frameMap2 = Frame(frameEntry, bg='#C8E6A8')
    frameMap2.pack(side="left", padx = 1)
    
    imageLabel2 = ImageLabel(frameNote2, width=250, height=100)
    imageLabel2.setImage('image/Search.gif')
    imageLabel2.bind('<Button-1>', Pressed)
    imageLabel2.pack(side = "left",  fill = X)


    global w
    w = Canvas(frameEntry,width = 5, height=100, bg='#C8E6A8')
    w.pack(side='left', anchor='n', expand=True, fill="both")

    global imageLabel4
    imageLabel4 = ImageLabel(frameEntry, width=120, height=100)
    imageLabel4.setImage('image/map.gif')
    imageLabel4.pack(side = "left", fill = "both")


def Check_Box_B():
    global GBName_CheckButton
    if chkBValue.get() == 1:
        chkGValue.set(0)
        GBName_CheckButton = True

    GraphUpdate()

def Check_Box_G():
    global GBName_CheckButton
    if chkGValue.get() == 1:
        chkBValue.set(0)
        GBName_CheckButton = False
    GraphUpdate()
def drawGraph(canvas, data, canvasWidth, canvasHeight): 
    canvas.delete("grim") # 기존 그림 지우기
    if data == None:
        return
    if not len(data): # 데이터 없으면 return
        canvas.create_text(canvasWidth/2,(canvasHeight/2), 
        text="", tags="grim") 
        return
    nData = len(data) # 데이터 개수, 최대값, 최소값 얻어 놓기
    nMax = max(data) 
    nMin = min(data)
    # background 그리기
    canvas.create_rectangle(0, 0, canvasWidth, canvasHeight, fill='#C8E6A8', tag="grim")

    if nMax == 0: # devide by zero 방지
        nMax=1
    rectWidth = (canvasWidth // nData) 
    # 데이터 1개의 폭. 
    bottom = canvasHeight - 2 # bar의 bottom 위치 
    maxheight = canvasHeight - 20 # bar의 최대 높이.(위/아래 각각 20씩 여유.)
    for i in range(nData): # 각 데이터에 대해.. 
        # max/min은 특별한 색으로.
        if nMax == data[i]: 
            color="#e893b0" 
        elif nMin == data[i]: 
            color='#cce8f4' 
        else: 
            color="#cce8f4" 
        curHeight = maxheight * data[i] / (nMax + 50) # 최대값에 대한 비율 반영
        top = bottom - curHeight # bar의 top 위치
        left = i * rectWidth # bar의 left 위치
        right = (i + 1) * rectWidth # bar의 right 위치
        canvas.create_rectangle(left, top, right, bottom, fill=color, tag="grim", activefill='#5ec8eb')
        # 위에 값, 아래에 번호. 
        canvas.create_text((left+right)//2, top-10, text=data[i], font = fontMidium3, tags="grim") 
        if GBName_CheckButton == True:
            canvas.create_text((left+right)//2, bottom+10, font = fontMidium3, text=Data[DataEnum.eName.value][ClosetList[G_bClosetEnum.B_Closet.value][i]], tags="grim")
        else:
            canvas.create_text((left+right)//2, bottom+10, font = fontMidium3, text=Data[DataEnum.eName.value][ClosetList[G_bClosetEnum.G_Closet.value][i]], tags="grim")
    
    
    
    
def event_for_listbox(event):
    global data
    global Lat
    global Lon
    global Lat_Data
    global Lon_Data
    global Data
    global listBox2
    global indexData
    global Name_Data
    global CurListBox3Index
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)

        Lat_Data = Data[DataEnum.eLat.value][indexData[index]]
        Lon_Data = Data[DataEnum.eLon.value][indexData[index]]
        Name_Data = Data[DataEnum.eName.value][indexData[index]]
        listBox2.delete(0, listBox2.size())
        _text = Data[DataEnum.eName.value][indexData[index]]
        CurListBox3Index = indexData[index]
        listN = 0
        if len(_text) > 15:
                if(len(_text[2:len(_text)].split('(', 1)) >= 2): # 2개이상 나눠진다
                    if len(_text.split('(', 1)[0]) > 3: #
                         listBox2.insert(listN, "화장실명 : " + _text.split('(', 1)[0])
                         listN = listN + 1
                    if len(_text.split('(', 1)[1]) > 3:
                         listBox2.insert(listN,   '(' + _text.split('(', 1)[1])
                         listN = listN + 1
                else:
                    listBox2.insert(listN, "화장실명 : " + Data[DataEnum.eName.value][indexData[index]])
                    listN = listN + 1
        else:
            listBox2.insert(listN, "화장실명 : " + Data[DataEnum.eName.value][indexData[index]])
            listN = listN + 1

        listBox2.insert(listN + 1, "주소 : " + Data[DataEnum.eAddress.value][indexData[index]])
        if Data[DataEnum.eNumber.value][indexData[index]] != None:
            if Number[index] != None:
                listBox2.insert(listN + 2, "전화번호 : " + Data[DataEnum.eNumber.value][indexData[index]])
            else:
                listBox2.insert(listN + 2, Data[DataEnum.eNumber.value][indexData[index]])
        if Data[DataEnum.eOpenTime.value][indexData[index]] != None:
            listBox2.insert(listN + 3, "개방시간 : " + Data[DataEnum.eOpenTime.value][indexData[index]])
        if Data[DataEnum.eGB_Check.value][indexData[index]] != None:
            listBox2.insert(listN + 4, "공용화장실여부 : " + Data[DataEnum.eGB_Check.value][indexData[index]])
        if Data[DataEnum.eB_Closet.value][indexData[index]] != None:
            listBox2.insert(listN + 5, "남성 변기수 : " + str(Data[DataEnum.eB_Closet.value][indexData[index]]))
        if Data[DataEnum.eG_Closet.value][indexData[index]] != None:
            listBox2.insert(listN + 6, "여성 변기수 : " + str(Data[DataEnum.eG_Closet.value][indexData[index]]))
        print(data)
    imageLabel.setImage('image/Email_Close.gif')

    


def getStr(s): 
    return '' if not s else s

def Big_ClosetData(indexData):
    global ClosetList

    for j in range(0, 2):
        maxIndex = 5
        if maxIndex > len(ClosetList[j]):
            maxIndex = len(ClosetList[j])
            if maxIndex == 0:
                ClosetList[j].insert(0, indexData)
                continue
        check_Insert = False
        for i in range(0, maxIndex):# 최대 5개까지만 검사
            if(Data[DataEnum.eB_Closet.value + j][ClosetList[j][i]] <= Data[DataEnum.eB_Closet.value + j][indexData]):
                ClosetList[j].insert(i, indexData)
                check_Insert = True
                break
                
        if  maxIndex < 5 and check_Insert == False:
            ClosetList[j].insert(maxIndex, indexData)
    return
def GraphUpdate():
    ListClosetN = []
    for i in range(0, 2):
        ClosetList[i] = ClosetList[i][0:5]
    for i in range(0, 2):
        print(ClosetList[i])

    if chkBValue.get() == 1:
        if  len(ClosetList[G_bClosetEnum.B_Closet.value]) != 0:
            for t in range(0, len(ClosetList[G_bClosetEnum.B_Closet.value])):
                ListClosetN.append(Data[DataEnum.eB_Closet.value][ClosetList[G_bClosetEnum.B_Closet.value][t]])
    if chkGValue.get() == 1:
        if  len(ClosetList[G_bClosetEnum.G_Closet.value]) != 0:
            for t in range(0, len(ClosetList[G_bClosetEnum.G_Closet.value])):
                ListClosetN.append(Data[DataEnum.eG_Closet.value][ClosetList[G_bClosetEnum.G_Closet.value][t]])
        
    drawGraph(w, ListClosetN, 438, 80) 
    
def ComboChange(self):
    # 시도 자르기
    global ClosetList
    for i in range(0, 2):
        ClosetList[i].clear()
    #만약 아래 콤보값과 같으면 리스트 박스에 넣기
    SearchCity(SearchListBox.get())
    GraphUpdate()



def SearchCity(city):
    from urllib.request import urlopen # 원격에서 가져오기
    from xml.etree import ElementTree
    
    global listBox
    global Lat
    global Lon
    global Name
    global Data
    global indexData
    global InputLabel
    global chkValue
    InputLabel.delete(0, 'end')
    indexData.clear()
    listBox.delete(0,listBox.size())
    listBox2.delete(0, listBox2.size())
    key = '50e822b566c5445e99f7d7582aea21ec' 
    Index = 11
    Type = 'xml'
    pSize = '1000'
    t = 1
    chkValue.set(0)
    for i in range(0, 7):
        Data[i].clear()
    for n in range(11):
        Index = str(n)
        url = 'https://openapi.gg.go.kr/Publtolt?key='\
        + key+'&pIndex=' + Index + '&Type=' + Type + '&pSize=' + pSize
        response = urlopen(url).read()

        strxml = response.decode('utf-8') # xml 해석하기
        parseData = ElementTree.fromstring(strxml)
    
        elements = parseData.iter('row')

        for item in elements:
            part_el = item.find('REFINE_LOTNO_ADDR')
            if item.find('REFINE_ROADNM_ADDR').text == None:
                continue
            strings = item.find('REFINE_ROADNM_ADDR').text.split(' ', 2)
            #print(checkbox)
            
            if strings[1] != city or part_el.text == None:
                continue
            else:
                _text = '[' + str(t) + '] ' + \
                getStr(item.find('PBCTLT_PLC_NM').text)
                if len(_text) > 15:
                    if(_text[10:len(_text)].split('(', 1) != None):
                        if len(_text.split('(', 1)[0]) > 3:
                            _text = _text.split('(', 1)[0]
                    
                listBox.insert(t-1, _text)
                
                Data[DataEnum.eName.value].insert(t - 1, item.find('PBCTLT_PLC_NM').text)
                Data[DataEnum.eAddress.value].insert(t - 1, item.find('REFINE_ROADNM_ADDR').text)
                Data[DataEnum.eNumber.value].insert(t - 1, item.find('MANAGE_INST_TELNO').text)
                Data[DataEnum.eOpenTime.value].insert(t - 1, item.find('OPEN_TM_INFO').text)
                Data[DataEnum.eLat.value].insert(t - 1, item.find('REFINE_WGS84_LAT').text)
                Data[DataEnum.eLon.value].insert(t - 1, item.find('REFINE_WGS84_LOGT').text)
                Data[DataEnum.eGB_Check.value].insert(t - 1, item.find('MALE_FEMALE_TOILET_YN').text)
                Data[DataEnum.eB_Closet.value].insert(t - 1, (int)(item.find('MALE_WTRCLS_CNT').text) + (int)(item.find('MALE_UIL_CNT').text))
                Data[DataEnum.eG_Closet.value].insert(t - 1, (int)(item.find('FEMALE_WTRCLS_CNT').text))

                Big_ClosetData(t - 1)
                indexData.append(t - 1)
                t = t+1

            
# 검색했을때
def Search_Name():
    from urllib.request import urlopen # 원격에서 가져오기
    from xml.etree import ElementTree
    global listBox
    global listBox2
    global Data
    global indexData
    global ClosetList
    listBox.delete(0, listBox.size())
    listBox2.delete(0, listBox2.size())
    indexData.clear()
    for i in range(0, 2):
        ClosetList[i].clear()
    j = 0
    for i in range(0, len(Data[DataEnum.eName.value])):
        if InputLabel.get() in Data[DataEnum.eName.value][i]:
            _text = '[' + str(j + 1) + '] ' + \
                Data[DataEnum.eName.value][i]
            if len(_text) > 15:
                if(_text[10:len(_text)].split('(', 1) != None):
                    if len(_text.split('(', 1)[0]) > 3:
                        _text = _text.split('(', 1)[0]         
            
            listBox.insert(j, _text)
            Big_ClosetData(i)
            indexData.append(i)
            j = j + 1
    GraphUpdate()

def Check_Public():
    global listBox2
    global indexData

    if chkValue.get() == 1: #체크 박스 누름
        indexData_Save = []

        j = 0
        for i in range(0, listBox.size()):
            if InputLabel.get() in Data[DataEnum.eName.value][indexData[i]] and Data[DataEnum.eGB_Check.value][indexData[i]] == "N":
                j = j + 1
                indexData_Save.append(indexData[i])
                
        listBox.delete(0, listBox.size())
        listBox2.delete(0, listBox2.size())
        for t in range(0, len(indexData_Save)):
            _text = '[' + str(t + 1) + '] ' + \
                Data[DataEnum.eName.value][indexData_Save[t]]
            listBox.insert(t, _text)
        
        indexData.clear()
        indexData = indexData_Save
    else:
        listBox.delete(0, listBox.size())
        listBox2.delete(0, listBox2.size())
        indexData.clear()
        j = 0
        for i in range(0, len(Data[DataEnum.eName.value])):
            if InputLabel.get() in Data[DataEnum.eName.value][i]:
                _text = '[' + str(j + 1) + '] ' + \
                     Data[DataEnum.eName.value][i]
                listBox.insert(j, _text)
                indexData.append(i)
                j = j + 1

def MailButton(self):
    if str(listBox2.get(0)) == '':    #보낼 메일 정보가 없으면
       msg.showinfo("Information", "메일 보낼 정보가 없습니다.")
       return
    #메일 잘못 입력하면 체크 => @기준으로
    str1 = ''
    for i in range(0,listBox2.size()):
        str1 = str1 + str(listBox2.get(i)) +'\n'
    msgse = MIMEText(str1) 
    msgse['Subject'] = '제목: 공중화장실 데이터'
    sendMail('mongjinjin@tukorea.ac.kr', InputEmail.get(), msgse)
    imageLabel.setImage('image/Email.gif')

from email.mime.text import MIMEText
def sendMail(fromAddr, toAddr, msg):
    import smtplib # 파이썬의 SMTP 모듈
    # 메일 서버와 connect하고 통신 시작
    s = smtplib.SMTP("smtp.gmail.com", 587) # SMTP 서버와 연결
    s.starttls() # SMTP 연결을 TLS (Transport Layer Security) 모드로 전환
    # 앱 password 이용
    s.login('mongjinjin@tukorea.ac.kr', 'jgbnfkhevztwosia') 
    s.sendmail(fromAddr , [toAddr], msg.as_string()) 
    s.close()

def Pressed(self):
    global Name_Data
    global Lat_Data
    global Lon_Data
    # if str(listBox2.get(0)) == '':    #보낼 정보가 없으면
    #    msg.showinfo("Information", "지도가 보일 클릭없음")
    #    return
    
    # Create a Map with Folium and Leaflet.js (위도 경도 지정) 
    if Lat_Data  == None or Lon_Data == None: # 둘 중 하나가 None이면
        msg.showinfo("Information", "해당 위도 경도가 존재하지 않습니다.")
        return
    
    map_osm = folium.Map(location=[Lat_Data,Lon_Data], zoom_start=18)
    folium.Circle(location=[Lat_Data,Lon_Data], radius = 5, fill = 'blue').add_to(map_osm)
    # 마커 지정
    folium.Marker([Lat_Data,Lon_Data], popup= Name_Data).add_to(map_osm)
    # html 파일로 저장
    map_osm.save('osm.html')
    webbrowser.open_new('osm.html')

def Book_Mark(Data):
    book_Mark.append()
    map_osm = folium.Map(location=[Lat_Data,Lon_Data], zoom_start=18)
    folium.Circle(location=[Lat_Data,Lon_Data], radius = 5, fill = 'blue').add_to(map_osm)
    # 마커 지정
    folium.Marker([Lat_Data,Lon_Data], popup= Name_Data).add_to(map_osm)
    # html 파일로 저장
    map_osm.save('osm.html')
    webbrowser.open_new('osm.html')

def Favorit_ButtonEvt():
    if str(listBox2.get(0)) == '':    #보낼 메일 정보가 없으면
       msg.showinfo("Information", "즐겨찾기에 추가할 정보가 없습니다.")
       return
    for i in range (0, listBox3.size()):  #중복되는 값이 있으면
        if listBox3.get(i) == Data[DataEnum.eName.value][CurListBox3Index]:
            msg.showinfo("Information", "중복되는 값이 존재합니다.")
            return    
    listBox3.insert(listBox3.size(), Data[DataEnum.eName.value][CurListBox3Index])
    Favori_List.append((Data[DataEnum.eLat.value][CurListBox3Index], Data[DataEnum.eLon.value][CurListBox3Index]))
def Book_MarkListClick(event):
    global Lat_Data
    global Lon_Data
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        Lat_Data = Favori_List[index][0]
        Lon_Data = Favori_List[index][1]

InitScreen()
    
g_Tk.mainloop()

    
from msilib.schema import CheckBox, ListBox
from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
import folium
import webbrowser
from tkinter import messagebox as msg
g_Tk = Tk()
g_Tk.geometry("900x700+450+100")

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

              #B  G
ClosetList = [[], []]
#       0       1       2       3          4   5    6           7          8
Data = [Name, Address, Number, OpenTime, Lat, Lon, GB_Check, B_Closet, G_Closet]
Lat_Data = 0.0
Lon_Data = 0.0
Name_Data = ""

text =""
data =""

fontMidium= font.Font(g_Tk, size = 15, weight='bold', family='경기천년제목 Medium')
fontMidium2= font.Font(g_Tk, size = 16, weight='bold', family='경기천년제목 Medium')
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
    frameTitle = Frame(g_Tk, padx = 10, pady=10, bg='#009933')
    frameTitle.pack(fill='x')
    frameCombo = Frame(g_Tk, pady=10, bg='#009933')
    frameCombo.pack(side='top', fill='x')
    frameCheck = Frame(g_Tk, pady=10, bg='#009933')
    frameCheck.pack(side='top', fill='x')
    frameMail = Frame(g_Tk,padx = 15, pady=10, bg='#009933')
    frameMail.pack(side='top', fill='x')
    frameEntry = Frame(g_Tk,padx=8.8, pady=10, bg='#009933')
    frameEntry.pack(side="top", fill="x")
    frameList = Frame(g_Tk, padx=30, pady=10, bg='#009933')
    frameList.pack(side="top", fill="both", expand=True)
    frameMap = Frame(g_Tk, padx=10, pady=10, bg='#009933')
    frameMap.pack(side="bottom", fill="both", expand=True)
#경기천년제목 Medium

    # MainText = Label(frameTitle, font = fontTitle, text="[공중 화장실 찾기 App]")
    # MainText.pack(anchor="center", fill="both")

    global chkValue
    global CheckButton
    chkValue = IntVar()
    
    CheckButton = ttk.Checkbutton(frameCombo, text="공용화장실여부", variable=chkValue, command = Check_Public).pack(side='left')
    print(chkValue.get())

    global SearchListBox 
    slist = ["가평군", "고양시", "과천시","광명시", "광주시", "구리시", 
             "군포시", "김포시", "남양주시", "동두천시", "부천시", "수원시", 
             "성남시", "시흥시", "안산시", "안성시", "안양시", "양주시", 
             "양평군", "여주시", "연천군", "오산시", "용인시", "의왕시", 
             "의정부시", "이천시", "파주시", "포천군", "평택시", "하남시",
             "화성시"] 
    SearchListBox = ttk.Combobox(frameCombo, values = slist)
    SearchListBox.set('시/군 선택')    
    SearchListBox.pack(side='left', padx= 5, expand=False )
     
    SearchListBox.bind("<<ComboboxSelected>>", ComboChange)
            
              
    #for i, s in enumerate(slist): 
     #   SearchListBox.insert(i, s)
    
    
    SearchButton = Button(frameEntry, font=fontMidium, \
           text='검색', command = Search_Name)
    SearchButton.pack(side='right', padx= 6, expand=False, fill='y')

    global InputLabel 
    InputLabel = Entry(frameEntry, font = fontMidium, \
            width = 26, borderwidth = 12, relief = 'flat')
    InputLabel.pack(side="right", padx= 10, expand = False)
    global imageLabel
    imageLabel = ImageLabel(frameCombo, width=55, height=55)
    imageLabel.setImage('Email_Close.gif')
    imageLabel.bind('<Button-1>', MailButton)
    imageLabel.pack(side = "right", padx= 15)


    imageLabel3 = ImageLabel(frameTitle, width=860, height=150)
    imageLabel3.setImage('AppName.gif')
    imageLabel3.pack(side = "top", expand = False)

    global InputEmail 
    InputEmail = Entry(frameCombo, font = fontMidium, \
            width = 30, borderwidth = 12, relief = 'flat')
    InputEmail.pack(side="right", pady = 20, expand = False)
    
    global listBox
    LBScrollbar = Scrollbar(frameList)
    listBox = Listbox(frameList, selectmode='extended',\
    font=fontMidium, width=3, height=15, \
    borderwidth=12, relief='ridge', yscrollcommand=LBScrollbar.set)
    listBox.bind('<<ListboxSelect>>', event_for_listbox)
    listBox.pack(side='left', anchor='n', expand=True, fill="x")
    LBScrollbar.pack(side='left', fill='y')
    LBScrollbar.config(command=listBox.yview)
    
    global listBox2
    listBox2 = Listbox(frameList, selectmode='extended',\
    font=fontMidium, width=5, height=7, \
    borderwidth=12, background = 'skyblue', relief='flat', yscrollcommand=LBScrollbar.set)
    listBox2.pack(side='left', anchor='n', expand=True, fill="x")

    frameMap2 = Frame(frameEntry, bg='#009933')
    frameMap2.pack(side="left")
    
    imageLabel2 = ImageLabel(frameMap2, width=150, height=100)
    imageLabel2.setImage('map.gif')
    imageLabel2.bind('<Button-1>', Pressed)
    imageLabel2.pack(side = "left", fill = X)
    
    global w
    w = Canvas(frameEntry,width = 5, height=100, bg='green')
    w.pack(side='left', anchor='n', expand=True, fill="x")
    drawGraph(w, [10, 67, 9, 15], 250, 100) 

def drawGraph(canvas, data, canvasWidth, canvasHeight): 
    canvas.delete("grim") # 기존 그림 지우기
    if not len(data): # 데이터 없으면 return
        canvas.create_text(canvasWidth/2,(canvasHeight/2), 
        text="No Data", tags="grim") 
        return
    nData = len(data) # 데이터 개수, 최대값, 최소값 얻어 놓기
    nMax = max(data) 
    nMin = min(data)
    # background 그리기
    canvas.create_rectangle(0, 0, canvasWidth, canvasHeight, fill='white', tag="grim")

    if nMax == 0: # devide by zero 방지
        nMax=1
    rectWidth = (canvasWidth // nData) 
    # 데이터 1개의 폭. 
    bottom = canvasHeight - 2 # bar의 bottom 위치 
    maxheight = canvasHeight - 4 # bar의 최대 높이.(위/아래 각각 20씩 여유.)
    for i in range(nData): # 각 데이터에 대해.. 
        # max/min은 특별한 색으로.
        if nMax == data[i]: 
            color="red" 
        elif nMin == data[i]: 
            color='blue' 
        else: 
            color="grey" 
        curHeight = maxheight * data[i] / nMax # 최대값에 대한 비율 반영
        top = bottom - curHeight # bar의 top 위치
        left = i * rectWidth # bar의 left 위치
        right = (i + 1) * rectWidth # bar의 right 위치
        canvas.create_rectangle(left, top, right, bottom, fill=color, tag="grim", activefill='yellow')
        # 위에 값, 아래에 번호. 
        canvas.create_text((left+right)//2, top-10, text=data[i], tags="grim") 
        canvas.create_text((left+right)//2, bottom+10, text=i+1, tags="grim")
    
    
    
    
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
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)

        Lat_Data = Data[4][indexData[index]]
        Lon_Data = Data[5][indexData[index]]
        Name_Data = Data[0][indexData[index]]
        listBox2.delete(0, 3)
        listBox2.insert(0, "화장실명:" + Data[0][indexData[index]])
        listBox2.insert(1, "소재지도로명주소:" + Data[1][indexData[index]])
        if Number[index] != None:
            listBox2.insert(2, "전화번호:" + Data[2][indexData[index]])
        else:
            listBox2.insert(2, Data[2][indexData[index]])

        listBox2.insert(3, "개방시간:" + Data[3][indexData[index]])
        listBox2.insert(3, "개방시간:" + Data[6][indexData[index]])
        print(data)
    imageLabel.setImage('Email_Close.gif')

    


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
        for i in range(0, maxIndex):# 최대 5개까지만 검사
            if(ClosetList[j][i] < Data[7 + j][indexData]):
                ClosetList[j].insert(i, indexData)
                break

    return 
    
def ComboChange(self):
    # 시도 자르기
    global ClosetList
    for i in range(0, 2):
        ClosetList[i].clear()
    #만약 아래 콤보값과 같으면 리스트 박스에 넣기
    SearchCity(SearchListBox.get())
    for i in range(0, 2):
        print(ClosetList[i])
    if  len(ClosetList) != 0:
        drawGraph(w, [10, 67, 9, 15], 250, 100) 

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
                listBox.insert(t-1, _text)
                
                Data[0].insert(t - 1, item.find('PBCTLT_PLC_NM').text)
                Data[1].insert(t - 1, item.find('REFINE_ROADNM_ADDR').text)
                Data[2].insert(t - 1, item.find('MANAGE_INST_TELNO').text)
                Data[3].insert(t - 1, item.find('OPEN_TM_INFO').text)
                Data[4].insert(t - 1, item.find('REFINE_WGS84_LAT').text)
                Data[5].insert(t - 1, item.find('REFINE_WGS84_LOGT').text)
                Data[6].insert(t - 1, item.find('MALE_FEMALE_TOILET_YN').text)
                Data[7].insert(t - 1, (int)(item.find('MALE_WTRCLS_CNT').text) + (int)(item.find('MALE_UIL_CNT').text))
                Data[8].insert(t - 1, (int)(item.find('FEMALE_WTRCLS_CNT').text))

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
    listBox.delete(0, listBox.size())
    listBox2.delete(0, listBox2.size())
    indexData.clear()
    j = 0
    for i in range(0, len(Data[0])):
        if InputLabel.get() in Data[0][i]:
            listBox.insert(j, Data[0][i])
            indexData.append(i)
            listBox2
            j = j + 1

def Check_Public():
    global listBox2
    global indexData

    if chkValue.get() == 1: #체크 박스 누름
        indexData_Save = []

        j = 0
        for i in range(0, listBox.size()):
            if InputLabel.get() in Data[0][i] and Data[6][indexData[i]] == "Y":
                j = j + 1
                indexData_Save.append(indexData[i])
                
        listBox.delete(0, listBox.size())
        listBox2.delete(0, listBox2.size())
        for t in range(0, len(indexData_Save)):
            listBox.insert(t, Data[0][indexData_Save[t]])
        
        indexData.clear()
        indexData = indexData_Save
    else:
        listBox.delete(0, listBox.size())
        listBox2.delete(0, listBox2.size())
        indexData.clear()
        j = 0
        for i in range(0, len(Data[0])):
            if InputLabel.get() in Data[0][i]:
                listBox.insert(j, Data[0][i])
                indexData.append(i)
                listBox2
                j = j + 1

def MailButton(self):
    global data
    print(data)
    msg = MIMEText(data) 
    msg['Subject'] = '제목: 공중화장실 데이터'
    sendMail('mongjinjin@tukorea.ac.kr', InputEmail.get(), msg)
    imageLabel.setImage('Email.gif')

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
    # Create a Map with Folium and Leaflet.js (위도 경도 지정) 
    if Lat_Data  == None or Lon_Data == None: # 둘 중 하나가 None이면
        msg.showinfo("Information", "해당 위도 경도가 존재하지 않습니다.")
        return
    
    map_osm = folium.Map(location=[Lat_Data,Lon_Data], zoom_start=13)
    # 마커 지정
    folium.Marker([Lat_Data,Lon_Data], popup= Name_Data).add_to(map_osm)
    # html 파일로 저장
    map_osm.save('osm.html')
    webbrowser.open_new('osm.html')


InitScreen()

g_Tk.mainloop()

    
from msilib.schema import ListBox
from tkinter import *
from tkinter import font
import folium
import webbrowser
from tkinter import messagebox as msg
g_Tk = Tk()
g_Tk.geometry("900x700+450+100")

text =""
data =""

Lat_Data = 0.0
Lon_Data = 0.0
Lat = []
Lon = []

Name = []
Name_Data = ""
fontMidium= font.Font(g_Tk, size = 15, weight='bold', family='경기천년제목 Medium')
fontMidium2= font.Font(g_Tk, size = 16, weight='bold', family='경기천년제목 Medium')

class ImageLabel(Label):
    def __init__(self, parent, filenameOrUrl = None, width = 0, height = 0):
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
    frameTitle = Frame(g_Tk, padx =10, pady=10, bg='#009933')
    frameTitle.pack(side="top", fill="x")
    frameCombo = Frame(g_Tk, pady=10, bg='#009933')
    frameCombo.pack(side='top', fill='x')
    frameMail = Frame(g_Tk,padx = 15, pady=10, bg='#009933')
    frameMail.pack(side='top', fill='x')
    frameEntry = Frame(g_Tk,padx=10, pady=10, bg='#009933')
    frameEntry.pack(side="top", fill="x")
    frameList = Frame(g_Tk, padx=10, pady=10, bg='#009933')
    frameList.pack(side="top", fill="both", expand=True)
    frameMap = Frame(g_Tk, padx=10, pady=10, bg='#009933')
    frameMap.pack(side="bottom", fill="both", expand=True)
#경기천년제목 Medium
    MainText = Label(frameTitle, font = fontTitle, text="[공중 화장실 찾기 App]")
    MainText.pack(anchor="center", fill="both")
    global SearchListBox 
    LBScrollbar = Scrollbar(frameCombo)
    SearchListBox = Listbox(frameCombo, \
        font=fontMidium2, activestyle='none', 
        width=10, height=1, borderwidth=12, relief='flat', 
        yscrollcommand=LBScrollbar.set) 
    
    SearchButton = Button(frameEntry, font=fontMidium, \
           text='검색', command = onSearch)
    SearchButton.pack(side='right', padx=10, expand=False, fill='y')

    global InputLabel 
    InputLabel = Entry(frameEntry, font = fontMidium, \
            width = 26, borderwidth = 12, relief = 'flat')
    InputLabel.pack(side="right", padx= 0, expand = False)

    global InputEmail 
    InputEmail = Entry(frameCombo, font = fontMidium, \
            width = 46, borderwidth = 12, relief = 'flat')
    InputEmail.pack(side="right", padx= 71.5, pady = 20, expand = False)
    

    
    global listBox
    LBScrollbar = Scrollbar(frameList)
    listBox = Listbox(frameList, selectmode='extended',\
    font=fontMidium, width=10, height=15, \
    borderwidth=12, relief='ridge', yscrollcommand=LBScrollbar.set)
    listBox.bind('<<ListboxSelect>>', event_for_listbox)
    listBox.pack(side='left', anchor='n', expand=True, fill="x")
    LBScrollbar.pack(side='left', fill='y')
    LBScrollbar.config(command=listBox.yview)
    
    global listBox2
    listBox2 = Listbox(frameList, selectmode='extended',\
    font=fontMidium, width=10, height=15, \
    borderwidth=12, relief='ridge', yscrollcommand=LBScrollbar.set)
    listBox2.bind('<<ListboxSelect>>', event_for_listbox)
    listBox2.pack(side='left', anchor='n', expand=True, fill="x")
    
    
    imageLabel = ImageLabel(frameCombo, width=47, height=45)
    imageLabel.setImage('Email.gif')
    imageLabel.bind('<Button-1>', MailButton)
    imageLabel.pack(side = "right", fill = X)

    frameMap2 = Frame(g_Tk, bg='#009933')
    frameMap2.pack(side="bottom")
    
    imageLabel2 = ImageLabel(frameMap2, width=150, height=100)
    imageLabel2.setImage('map.gif')
    imageLabel2.bind('<Button-1>', Pressed)
    imageLabel2.pack(side = "bottom", fill = X)
    
def event_for_listbox(event):
    global data
    global Lat
    global Lon
    global Lat_Data
    global Lon_Data
    global Name_Data
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        Lat_Data = Lat[index]
        Lon_Data = Lon[index]
        Name_Data = Name[index]
        print(data)

        
def onSearch(): # "검색" 버튼 이벤트처리
    global SearchListBox
    listBox.yview
    sels = SearchListBox.curselection()
    iSearchIndex = \
        0 if len(sels) == 0 else SearchListBox.curselection()[0]
    Search(iSearchIndex)


def getStr(s): 
    return '' if not s else s

def Search(num):
    from urllib.request import urlopen # 원격에서 가져오기
    from xml.etree import ElementTree
    
    global listBox
    global Lat
    global Lon
    global Name

    listBox.delete(0,listBox.size())

    key = '50e822b566c5445e99f7d7582aea21ec' 
    Index = 11
    Type = 'xml'
    pSize = '1000'
    check = 0
    out = 0
    i = 1
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
                                
            if part_el.text == None:
                continue
            if InputLabel.get() in part_el.text:
                _text = '[' + str(i) + '] ' + \
                getStr(item.find('PBCTLT_PLC_NM').text)

                listBox.insert(i-1, _text)
                Lat.insert(i - 1, item.find('REFINE_WGS84_LAT').text)
                Lon.insert(i - 1, item.find('REFINE_WGS84_LOGT').text)
                Name.insert(i - 1, item.find('PBCTLT_PLC_NM').text)
                i = i+1
               
                
        
            



def MailButton(self):
    global data
    print(data)
    msg = MIMEText(data) 
    msg['Subject'] = '제목: 공중화장실 데이터'
    sendMail('mongjinjin@tukorea.ac.kr', InputEmail.get(), msg)

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
    global Lat_Data
    global Lon_Data
    # Create a Map with Folium and Leaflet.js (위도 경도 지정) 
    if Lat_Data  == None or Lon_Data == None: # 둘 중 하나가 None이면
        msg.showinfo("Information", "해당 위도 경도가 존재하지 않습니다.")
        return
    
    map_osm = folium.Map(location=[Lat_Data,Lon_Data], zoom_start=13)
    # 마커 지정
    folium.Marker([Lat_Data,Lon_Data],
    popup= Name_Data).add_to(map_osm)
    # html 파일로 저장
    map_osm.save('osm.html')
    webbrowser.open_new('osm.html')


InitScreen()

g_Tk.mainloop()

    
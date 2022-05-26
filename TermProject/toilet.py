from msilib.schema import ListBox
from tkinter import *
from tkinter import font

g_Tk = Tk()
g_Tk.geometry("500x700+450+100")

text =""

def InitScreen():
    fontTitle = font.Font(g_Tk, size=18, weight='bold', family='고딕체')
    fontNormal = font.Font(g_Tk, size = 15, weight='bold')
    frameTitle = Frame(g_Tk, padx=10, pady=10, bg='#ff0000')
    frameTitle.pack(side="top", fill="x")
    frameCombo = Frame(g_Tk,padx = 15, pady=10, bg='#00ff00')
    frameCombo.pack(side='top', fill='x')
    frameEntry = Frame(g_Tk,padx=10, pady=10, bg='#0000ff')
    frameEntry.pack(side="top", fill="x")
    frameList = Frame(g_Tk, padx=10, pady=10, bg='#ffff00')
    frameList.pack(side="top", fill="both", expand=True)
    frameMap = Frame(g_Tk, padx=10, pady=10, bg='#ffffff')
    frameMap.pack(side="bottom", fill="both", expand=True)

    MainText = Label(frameTitle, font = fontTitle, text="[공중 화장실 찾기 App]")
    MainText.pack(anchor="center", fill="both")
    global SearchListBox 
    LBScrollbar = Scrollbar(frameCombo)
    SearchListBox = Listbox(frameCombo, \
        font=fontNormal, activestyle='none', 
        width=10, height=1, borderwidth=12, relief='flat', 
        yscrollcommand=LBScrollbar.set) 
    slist = ["서울특별시", "경기도", "인천광역시"]
    for i, s in enumerate(slist): 
        SearchListBox.insert(i, s)
    SearchListBox.pack(side='left', ipadx= 5, expand=False, \
                            )
    LBScrollbar.pack(side="left")
    LBScrollbar.config(command=SearchListBox.yview) 
    
    sendEmailButton = Button(frameCombo, font = fontNormal, text='이메일', command = MailButton) 
    sendEmailButton.pack(side='right', padx=10, fill='y')
    
    global InputLabel 
    InputLabel = Entry(frameEntry, font = fontNormal, \
            width = 26, borderwidth = 12, relief = 'flat')
    InputLabel.pack(side="left", padx= 10, expand = False)
    
    SearchButton = Button(frameEntry, font=fontNormal, \
           text='검색', command = onSearch)
    SearchButton.pack(side='left', padx=10, expand=False, fill='y')
    
    global listBox
    LBScrollbar = Scrollbar(frameList)
    listBox = Listbox(frameList, selectmode='extended',\
    font=fontNormal, width=10, height=15, \
    borderwidth=12, relief='ridge', yscrollcommand=LBScrollbar.set)
    listBox.bind('<<ListboxSelect>>', event_for_listbox)
    listBox.pack(side='left', anchor='n', expand=True, fill="x")
    LBScrollbar.pack(side='right', fill='y')
    LBScrollbar.config(command=listBox.yview)
    
def event_for_listbox(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
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
    from xml.etree import ElementTree
    
    global listBox
    listBox.delete(0,listBox.size())
    
    text = ""
    if num == 0:
        text = "Seoul.xml"
    elif num == 1:
        text = "Incheon.xml"
    elif num == 2:
        text = "Gyeonggi.xml"

    with open(text, 'rb') as f:
        strXml = f.read().decode('utf-8')
        parseData = ElementTree.fromstring(strXml) 
    
    elements = parseData.iter('toilet')
    i = 1

    for item in elements:
        part_el = item.find('ADRES')

        if part_el.text == None:
            continue
        if InputLabel.get() not in part_el.text:
            continue
        
        _text = '[' + str(i) + '] ' + \
         getStr(item.find('NAME').text) + \
         ' : ' + getStr(item.find('ADRES').text) + \
         ' : ' + getStr(item.find('OPEN_TIME').text)
         
        listBox.insert(i-1, _text)
        i = i+1
       
def MailButton():
    msg = MIMEText(text) 
    msg['Subject'] = '제목: 공중화장실 데이터'
    sendMail('mongjinjin@tukorea.ac.kr', 'mongjinjin@naver.com', msg)
    
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
        
InitScreen()
g_Tk.mainloop()


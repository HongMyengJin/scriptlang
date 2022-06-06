from http.client import HTTPSConnection

conn = None
server = "openapi.naver.com"# 네이버 OpenAPI 서버
def connectOpenAPIServer(): 
    global conn, server 
    conn = HTTPSConnection(server) 
    conn.set_debuglevel(1)

def userURIBuilder(uri, **user): 
    str = uri + "?"
    for key in user.keys(): str += key + "=" + user[key] + "&"
    return str

def getBookDataFromISBN(isbn): 
    global server, conn
    client_id = "XXXXXXXXXXXXX" 
    client_secret = "YYYYYYYY"
    if conn == None : connectOpenAPIServer() # OpenAPI 접속
    #네어버에서 ISBN에 의한 도서정보 가져올 URL 생성
    uri = userURIBuilder("/v1/search/book_adv.xml", display="1", start="1", d_isbn=isbn)
    conn.request("GET", uri, None, #GET 요청
{"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    req = conn.getresponse()
    print (req.status)
    if int(req.status) == 200 : 
        print("Book data downloading complete!")
        return extractBookData(req.read()) 
        #요청이 성공이면 book 정보추출
    else: 
        print ("OpenAPI request has been failed!! please retry")
        return None

def extractBookData(strXml): #strXml은 OpenAPI 검색 결과 XML 문자열
    from xml.dom.minidom import parseString
    from xml.etree import ElementTree
    
    tree = ElementTree.fromstring(strXml)
    print (parseString(strXml.decode('utf-8')).toprettyxml()) # 내용확인용
    #"item" 하위의 "title" 찾기. # Note! 그냥 "title"은 찾으면 상단의 "title"도 검색되므로. 
    itemElements = tree.iter("item") # item 엘리먼트 리스트추출for item in itemElements:
    isbn = item.find(＂isbn＂) #isbn 검색
    title = item.find(＂title＂) #title 검색
    if len(title.text) > 0 : # AddBook()에 줄 수 있는 사전형식 반환
    return {"ISBN":isbn.text,"title":title.text}
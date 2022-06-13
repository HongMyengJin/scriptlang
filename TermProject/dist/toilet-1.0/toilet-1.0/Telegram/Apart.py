
from urllib.request import urlopen # 원격에서 가져오기
from xml.dom.minidom import parseString # xml 해석하기
# 공공데이터 포털 Key
Index = '2'
Type = 'xml'
pSize = '200'
key = '50e822b566c5445e99f7d7582aea21ec' 

for n in range(11):
    Index = str(n)
    url = 'https://openapi.gg.go.kr/Publtolt?key='\
        + key+'&pIndex=' + Index + '&Type=' + Type + '&pSize=' + pSize
    response = urlopen(url).read()
    strxml = response.decode('utf-8') # xml 해석하기
    print(parseString(strxml).toprettyxml())


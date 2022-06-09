from urllib.request import urlopen # 원격에서 가져오기
from xml.dom.minidom import parseString # xml 해석하기
# 공공데이터 포털 Key
key = 'g+qBbnM0l4QVNO6kq/robYeLHLTDNLE6kswE/3AzzLgd3ITCBkam846UhiYvGCW1yO87/EpjoENnbn4xGNLJ0w=='
url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?_wadl&type=xml'\
    'LAWD_CD=11545&'\
    'DEAL_YMD=202101&'\
    'serviceKey='+key
response = urlopen(url).read()
strxml = response.decode('utf-8') # xml 해석하기
print(parseString(strxml).toprettyxml())

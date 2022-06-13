#!/usr/bin/python
# coding=utf-8
import sys
import telepot
from pprint import pprint # 데이터를 읽기 쉽게 출력
from urllib.request import urlopen
import traceback
from xml.etree import ElementTree
from xml.dom.minidom import parseString

Type = 'xml'
pSize = '1000'
key = '50e822b566c5445e99f7d7582aea21ec' 

for n in range(11):
    Index = str(n)
    url = 'https://openapi.gg.go.kr/Publtolt?key='\
        + key+'&pIndex=' + Index + '&Type=' + Type + '&pSize=' + pSize
    response = urlopen(url).read()
    strxml = response.decode('utf-8') # xml 해석하기

key = '50e822b566c5445e99f7d7582aea21ec'
TOKEN = '5529657440:AAGR0XLgywk0b88G512odGm1yTbcpw2guAg' 
MAX_MSG_LENGTH = 300
baseurl ='https://openapi.gg.go.kr/Publtolt?key='+key
bot = telepot.Bot(TOKEN)

# loc_param: 지역코드, date_param: yyyymm
# 반환 : 거래 건 별로 문자열로 표현한 리스트. 
def getData(name_param, Male_FeMale_param):  # 이름과 공용여부
    res_list = [] 
    for n in range(0, 11):
        Index = str(n)
        url = 'https://openapi.gg.go.kr/Publtolt?key='+ key +'&pIndex=' + Index + '&Type=' + Type + '&pSize=' + pSize
        response = urlopen(url).read()
        strxml = response.decode('utf-8') # xml 해석하기
        tree = ElementTree.fromstring(strxml)
        row = ""
        items = tree.iter("row") # return list type
        for item in items: 
            name = item.find("PBCTLT_PLC_NM").text
            if name_param in name:
                row += "이름: " + name + '\n'
                if item.find("REFINE_ROADNM_ADDR").text != None:
                    row += "주소: " + item.find("REFINE_ROADNM_ADDR").text + '\n'
                if item.find("MALE_FEMALE_TOILET_YN").text != None:
                    row += "공용화장실: " + item.find("MALE_FEMALE_TOILET_YN").text + '\n'
                if item.find("REFINE_WGS84_LAT").text != None:
                    row += "위도: " + item.find("REFINE_WGS84_LAT").text + '\n'
                if item.find("REFINE_WGS84_LOGT").text != None:
                    row += "경도:getcityData" + item.find("REFINE_WGS84_LOGT").text + '\n'    
                if item.find("MANAGE_INST_TELNO").text != None:
                    row += "전화번호: " + item.find("MANAGE_INST_TELNO").text + '\n'       
                res_list.append(row) 
    return res_list
def getcityData(city_param):  # 이름과 공용여부
    res_list = [] 
    res_listN = 0
    for n in range(0, 11):
        Index = str(n)
        url = 'https://openapi.gg.go.kr/Publtolt?key='+ key +'&pIndex=' + Index + '&Type=' + Type + '&pSize=' + pSize
        response = urlopen(url).read()
        strxml = response.decode('utf-8') # xml 해석하기
        tree = ElementTree.fromstring(strxml)
        items = tree.iter("row") # return list type
        for item in items: 
            strings = item.find("PBCTLT_PLC_NM").text
            if item.find('REFINE_ROADNM_ADDR').text != None and item.find('REFINE_ROADNM_ADDR').text.split(' ', 2) != None:
                strings = item.find('REFINE_ROADNM_ADDR').text.split(' ', 2)
                GBstrings = item.find('MALE_FEMALE_TOILET_YN').text
            else:
                continue
            #print(checkbox)
            row = ""
            if strings[1] == city_param and GBstrings == 'N':
                if item.find("PBCTLT_PLC_NM").text != None:
                    row += "이름: " + item.find("PBCTLT_PLC_NM").text + '\n'
                if item.find("REFINE_ROADNM_ADDR").text != None:
                    row += "주소: " + item.find("REFINE_ROADNM_ADDR").text + '\n'
                if item.find("MALE_FEMALE_TOILET_YN").text != None:
                    row += "공용화장실: " + item.find("MALE_FEMALE_TOILET_YN").text + '\n'
                if item.find("REFINE_WGS84_LAT").text != None:
                    row += "위도: " + item.find("REFINE_WGS84_LAT").text + '\n'
                if item.find("REFINE_WGS84_LOGT").text != None:
                    row += "경도: " + item.find("REFINE_WGS84_LOGT").text + '\n'    
                if item.find("MANAGE_INST_TELNO").text != None:
                    row += "전화번호: " + item.find("MANAGE_INST_TELNO").text + '\n'       
                res_list.append(row)
                res_listN = res_listN + 1
                if res_listN > 9:
                    return  res_list
    return  res_list

def sendMessage(user, msg): 
    try:
        bot.sendMessage(user, msg) 
    except: # 예외 정보와 스택 트레이스 항목을 인쇄. 
        traceback.print_exception(*sys.exc_info(), file=sys.stdout)

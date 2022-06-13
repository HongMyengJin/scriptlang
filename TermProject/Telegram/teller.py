#!/usr/bin/python
# coding=utf-8
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
import re
from datetime import date, datetime
import noti


# name_param: 날짜, user: 사용자ID, Male_FeMale_param:남여 공용 여부
def replyAptData(name_param, user, Male_FeMale_param='Y'): 
    #print(user, name_param, Male_FeMale_param) 
    res_list = noti.getData( name_param, Male_FeMale_param )
# 하나씩 보내면 메세지 개수가 너무 많아지므로
# 300자까지는 하나의 메세지로 묶어서 보내기. 
    msg = '' 
    for r in res_list: 
        #print( str(datetime.now()).split('.')[0], r )
        if len(r+msg)+1>noti.MAX_MSG_LENGTH: 
            noti.sendMessage( user, msg ) 
            msg = r+'\n' 
        else: 
            msg += r+'\n'
    if msg: 
        noti.sendMessage( user, msg ) 
    else: 
        noti.sendMessage( user, '%s 기간에 해당하는 데이터가 없습니다.'%name_param)

def replyCityAptData(city_param, user): 
    #print(user, name_param, Male_FeMale_param) 
    res_list = noti.getcityData(city_param)
# 하나씩 보내면 메세지 개수가 너무 많아지므로
# 300자까지는 하나의 메세지로 묶어서 보내기. 
    msg = '' 
    for r in res_list: 
        #print( str(datetime.now()).split('.')[0], r )
        msg = r+'\n'
        noti.sendMessage( user, msg ) 
         
        # else: 
        #     msg += r+'\n'
    if msg: 
        # noti.sendMessage( user, msg )
        a = 1
    else: 
        noti.sendMessage( user, '%s 기간에 해당하는 데이터가 없습니다.'%city_param)

def save( user, Male_FeMale_param ): 
    conn = sqlite3.connect('users.db') 
    cursor = conn.cursor() 
    cursor.execute('CREATE TABLE IF NOT EXISTS \ users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    try: 
        cursor.execute('INSERT INTO users(user, location) VALUES ("%s", "%s")' % (user, Male_FeMale_param)) 
    except sqlite3.IntegrityError: 
        noti.sendMessage( user, '이미 해당 정보가 저장되어 있습니다.' ) 
        return
    else: 
        noti.sendMessage( user, '저장되었습니다.' ) 
        conn.commit()

def check( user ): 
    conn = sqlite3.connect('users.db') 
    cursor = conn.cursor() 
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, locationTEXT, PRIMARY KEY(user, location) )') 
    cursor.execute('SELECT * from users WHERE user="%s"' % user)
    for data in cursor.fetchall(): 
        row = 'id:' + str(data[0]) + ', location:' + data[1] 
        noti.sendMessage( user, row )

def handle(msg): 
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text': 
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.') 
        return
    text = msg['text'] 
    args = text.split(',')

    if text.startswith('정보검색') and len(args)>1: 
        print('try to 정보검색', args[1]) 
        replyAptData( args[1], chat_id, None )
    elif text.split(',', 1)[0] != None and text.split(',', 1)[0] == '지역별 비공용화장실 검색' and len(args)>1: 
        print('try to 지역별 비공용화장실 검색', args[1], args[1] ) 
        replyCityAptData( args[1], chat_id)    
    else: 
        noti.sendMessage(chat_id, '''모르는 명령어입니다.\n정보검색, [화장실명] 명령을 입력하세요.\n\n지역별 비공용화장실 검색, [지역] 명령을 입력하세요.\n''')
    

today = date.today() 
current_month = today.strftime('%Y%m')
print( '[',today,']received token :', noti.TOKEN )
from noti import bot
pprint( bot.getMe() )
bot.message_loop(handle)
print('Listening...') 
while 1: 
    time.sleep(10)
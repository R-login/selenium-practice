import time
from asyncio.windows_events import NULL
from os import system
from pprint import pprint
# d1 = {1:'1' ,1.1:1.1, False:'False', True:'True',None:'1',
#       3:'周双庆', '任雨桥':None , 34:(1,) ,35:[1],
#       36:{1:1}}
#
# import json
# json_text = json.dumps(d1,ensure_ascii=False,indent=4)
# print(json_text)
# print(type(json_text))
# dict_text = json.loads(json_text)
# # print(dict_text)
# # print(type(dict_text))
# list_1 = [1,2,3,4,5,6]
# list_2 = ['一','二','三','四','五','六','七']
# zip_list = dict(zip(list_1, list_2))
# str_1 = '123344534'
# set_1 = {1,2,3,4,5,6,6,5,4}
# s = {(1,),'周双庆',1,1.2,True,None}
# s.add(89)
# print(s.symmetric_difference(set_1))
# print(s.symmetric_difference_update(set_1))
# print(s)
# print(set_1)
# print(len(set_1))
# print(max(set_1))
# print(min(set_1))
# tuple_1 = (1,'123',[3,4],{5,6},7,8)
# ti = 1,2
# print(set(ti))
# print(list(ti))
# print(str(ti))
import os
# print(os.getcwd())
# print(os.listdir('C:\\tools\PyCharm 2025.3.3\data'))
# print(os.path.exists('C:\\tools\PyCharm 2025.3.3\data\\证据'))
# print(os.system('adb install ""C:\\Users\\15123\Desktop\安装\\'
#                 'app-google-release(14).apk""'))
# print(os.system('adb exec-out screencap -p > C:\\'
#                 'Users\\15123\Desktop\截图\screenshot.png'))

# print(time.gmtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
# from datetime import *
# print(datetime.utcnow())
# print(datetime.now())
# now = '2026-03-27 09:54:04'
# now_date = datetime.strptime(now, '%Y-%m-%d %H:%M:%S')
# print(datetime.strptime(now, '%Y-%m-%d %H:%M:%S'))
# utcnow = datetime.utcnow()
# print(utcnow)
# print(type(utcnow))
# print(datetime.strftime(utcnow, '%Y-%m-%d %H:%M:%S'))
# print(type(datetime.strftime(utcnow, '%Y-%m-%d %H:%M:%S')))
# print(now_date - timedelta())
# now_2 = '2025-03-26 08:53:04'
# now2_date = datetime.strptime(now_2, '%Y-%m-%d %H:%M:%S')
# print((now_date - now2_date).total_seconds())
from 证据.day_03 import Human

print(Human.skin)
a = Human()
a.eat()

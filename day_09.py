#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/3 15:12
def sing(n):
    print(threading.current_thread())
    for i in range(n):
        time.sleep(1)
        print('唱歌')
def dance(n):
    print(threading.current_thread())
    for i in range(n):
        time.sleep(1)
        print('跳舞')
import threading
import time
t1 = threading.Thread(target=sing,kwargs={'n':10})
t2 = threading.Thread(target=dance,args=(5,))
t1.start()
t2.start()
print(threading.enumerate())
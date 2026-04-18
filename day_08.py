#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/3 12:05
class exercise(object):
    def __enter__(f):
        f.card = '柜子卡'
        f.mao = '毛巾'
        print(f'拿到了{f.card}和{f.mao}')
        return f.mao
    def aaa(self):
        print('进行中')
    def __exit__(self,exc_type, exc_val, exc_tb):
        self.card = '柜子卡'
        self.mao = '毛巾'
        print(f'归还{self.card}和{self.mao}')

with exercise() as f:
    print(f)











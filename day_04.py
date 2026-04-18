#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/1 09:32
class NBA(object):

     def player(self):
        self.name = '任雨桥'
        print(f'{self.name}是NBA球员')
        print(id(self))

class CBA(NBA):

    def player(self):
        self.name = '刘泽坤'
        print(f'{self.name}是CBA球员')
        print(id(self))
        NBA.player(self)
n = NBA()
c = CBA()
c.player()

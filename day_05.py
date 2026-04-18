#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/1 12:02
class GrandPa(object):  # 父类1：爷爷有A驾照，可以开公交车
    def __init__(self):
        self.id = "A"

    def drive_A(self):
        print("拥有驾照%s，可以开公交车" % self.id)

class Father(object):    # 父类2：爸爸有B驾照，可以开货车
    def __init__(self):
        self.id = "B"

    def drive_B(self):
        print("拥有驾照%s，可以开货车" % self.id)

class Diver(GrandPa,Father):   # 子类，多继承：拥有驾照C，可以开小汽车
    def __init__(self):
        self.id = "C"

    def drive(self):
        Diver.__init__(self)
        print("拥有驾照%s，可以开汽车" % self.id)

    def drive_granpa(self):

        GrandPa.drive_A(GrandPa())


    def drive_father(self):

        Father.drive_B(Father())

if __name__ == '__main__':
    d = Diver()
    d.drive()
    d.drive_granpa()
    d.drive_father()
    Diver.drive(d)
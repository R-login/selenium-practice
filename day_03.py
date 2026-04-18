#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/3/30 09:57
from os import name


class Human(object):
    skin = '白色'
    def eat(self):
        self.bed = 'lvse'
        self.sleep()
        print('吃饭')

    def sleep(self):
        self.bed = '蓝色'
        print('睡觉')
        print(id(self))

    def conquer(self):
        self.id = 123
        print(self.skin)
        print('征服')

    def call(self,B):  # 定义实例方法
        self.tell = "18800010006"
        print(f"打电话给{self.tell}")
        B.test_b()
        print(B.b)


class B(object):
    def __init__(self,age,name):
        print("B类中的初始化方法")
        self.b = "B类的实例属性"
        print(age,name)

    @classmethod
    def test_a(cls):
        print('B类中的test_a方法')

    @classmethod
    def test_b(cls):
        print("B类中的实例方法")
        cls.test_a()
        B.test_a()

    def __str__(self):
        return self.b

b = B(3,24)
b.test_b()





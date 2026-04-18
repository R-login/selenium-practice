#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/2 09:21
# class Father(object):
#
#     age = 59
#     def name(self):
#         print('我是爸爸')
#
# class Mother(Father):
#     def name(self):
#         print('我是妈妈')
#
# class Son(Mother,):
#     def name(self):
#         super(Mother, Son().name())


class School(object):
    renshu = 1000
    gao_1 = 300
    gao_2 = 320
    gao_3 = 380

    @classmethod
    def update(cls,class_name):
        class_name = class_name[:2]
        if class_name == '高一':
            cls.gao_1 = cls.gao_1 + 1
        elif class_name == '高二':
            cls.gao_2 = cls.gao_2 + 1
        elif class_name == '高三':
            cls.gao_3 = cls.gao_3 + 1
        cls.renshu = cls.renshu + 1

class Student(School):
    def __init__(self,class_name):
        super().update(class_name)


s = Student('高三4班')
print('加入一名学生,现在学校总人数是%s,高一人数是%s,'
      '高二人数是%s,高三人数是%s' % (s.renshu,s.gao_1,s.gao_2,s.gao_3))

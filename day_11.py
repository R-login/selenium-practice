#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/4 13:21
import  os
# Desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
# file_path = os.path.join(Desktop_path, '内容.txt')
# ew_path = os.path.join(Desktop_path, "新歌列表.txt")
# os.rename(file_path, ew_path)
# # with open(file_path,'a',encoding='utf-8') as f:

    # if os.path.exists(file_path):
    #     print('存在')
    # else:
    #     print('不存在')
# os.rename(file_path, ew_path)
import xlrd
Desk_path = os.path.join(os.path.expanduser('~'), 'Desktop')
file_path = os.path.join(Desk_path, 'students.xlsx')
file_path2 = os.path.join(Desk_path, '桌子')
book_obj = xlrd.open_workbook(file_path)
sheet_1 =  book_obj.sheet_by_name('考试成绩')
rows = sheet_1.nrows
with open(file_path2,'w',encoding='utf-8') as f:
    for i in range(rows):
        data = sheet_1.row_values(i)
        list_obj = []
        for j in data:
            if isinstance(j,float):
                list_obj.append(str(int(j)))
            else:
                list_obj.append(str(j))

        f.write(",".join(list_obj) + '\n')



























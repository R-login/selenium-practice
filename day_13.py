#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/6 12:04
import re
# lst = ['万州1','万州2','万州3','万州好','万州5','万州6','万州7']
# for i in lst:
#     r = re.search('万州[0-9a-zA-Z好]',i)
#     if r:
#         print(r.group())
#     else:
#         print('%s匹配失败' % i)

# lst = ['049999-','0^23-12344560','026','905-','067-','022-','045-','056-']
# for i in lst:
#     r = re.match(r'[0]^[1-9]{2,4}-[1-9][0-9]{7,8}$', i)
#     if r:
#         print(r.group())
#     else:
#         print('%s匹配失败' % i)
# r = re.search(r"\d1*$","1111   11")
# print(r.group())
# r = re.search(r"(.)(.)(.)","1231   11")
# print(r.group())
# print(r.group(1))
# print(r.group(2))
# print(r.group(3))
lst = ["woniutest@163.com","woniutest@qq.com","woniutest163.com","qq.com"]
for i in lst:
    r = re.search("^[A-Za-z0-9]{6,12}@163|qq\.com$",i)
    if r:
        print(r.group())
    else:
        print("%s匹配失败" % i)

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/3 17:11
from logging import exception

try:
    print(a)

except BaseException as e:
    print('错了%s' % e)
else:
    print('对了')
finally:
    print('finally')

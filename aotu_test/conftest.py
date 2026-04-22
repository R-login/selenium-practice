#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/22 17:05
import pytest

@pytest.fixture(name="blue",scope="class")
def blue():
    print("前置")
    yield "浏览器驱动"
    print('后置')

@pytest.fixture(name="angel",scope="function")
def angel(request):
    print("前置1")
    data = request.param
    print(f"www{data[0]},{data[1]}")
    yield '浏览器对象'
    print('后置1')
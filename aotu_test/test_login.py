#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/21 13:58
import pytest
import os
import time

from 证据.aotu_test.conftest import blue


class TestDemo2(object):
    # ["username", "passwd"],

    @pytest.mark.parametrize("angel",
                             [["renyuqiao",123456],
                              (789,789)]
                              ,indirect=True)
    def test_login_01(self,angel):  # 测试方法中包含login，该条用例会被执行
        print(f'用户名')



    def test_02(self):
        assert False

    def test_sss(self):
        print("第六条测试用例")




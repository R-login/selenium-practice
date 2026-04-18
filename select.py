#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/11 14:21
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.select import Select
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
try:
    browser.get('https://www.baidu.com')
    button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#s-usersetting-top')))
    print(f"✅ 所有span加载完毕")
    button.click()
    button2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.s-user-setting-pfmenu')))
    spans = button2.find_elements(By.CSS_SELECTOR,'span')
    for index, span in enumerate(spans,start=1):
        if span.get_attribute("class") == "set":
            print(f"第{index}个span".center(30,'='))
            print(f'span的文本是{span.text}')
    A = button2.find_elements(By.CSS_SELECTOR,'a')
    for index, a in enumerate(A, start=1):
        if a.get_attribute("class") == "hide-feed" or a.get_attribute("class") == "show-feed" or a.get_attribute("class") == "red-point" or a.get_attribute("target") == "target":
            print(f'a的文本是{a.text}')



except Exception as e:
    print(f'❌ 程序出错了'.center(30,'='))
    print(f'报错信息是：',e)

finally:
    time.sleep(5)
    browser.quit()
    print(f'✅ 脚本执行完毕，退出浏览器')


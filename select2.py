#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/11 17:40
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
browser = webdriver.Chrome()
browser.get('https://sahitest.com/demo/selectTest.htm ')
browser.maximize_window()
try:
    wait = WebDriverWait(browser, 10)
    select1 = Select(wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#s1Id'))))
    print(f'✅ 定位到第一个下拉框')
    for index,select in enumerate(select1.options):
        print(f'第{index + 1}个下拉选项'.center(30,'='))
        print(f'选项文本是：{select.text}')
        select1.select_by_index(index)
        print(f"当前选中项：{select1.first_selected_option.text}\n")
        time.sleep(1)

    select2 = Select(wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#s2Id'))))
    print(f'✅ 定位到第二个下拉框')
    for index,select in enumerate(select2.options):
        print(f'第{index + 1}个下拉选项'.center(30, '='))
        print(f'选项文本是：{select.text}')
        select2.select_by_index(index)
        print(f"当前选中项：{select2.first_selected_option.text}\n")
        time.sleep(1)

    select3 = Select(wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#s3Id'))))
    print(f'✅ 定位到第三个下拉框')
    for index, select in enumerate(select3.options):
        print(f'第{index + 1}个下拉选项'.center(30, '='))
        print(f'选项文本是：{select.text}')
        select3.select_by_index(index)
        print(f"当前选中项：{select3.first_selected_option.text}\n")
        time.sleep(1)

    select4 = Select(wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#s4Id'))))
    print(f'✅ 定位到第四个下拉框')
    for index, select in enumerate(select4.options):
        print(f'第{index + 1}个下拉选项'.center(30, '='))
        print(f'选项文本是：{select.text}')
        select4.deselect_all()
        select4.select_by_index(index)
        print(f"当前选中项：{select4.first_selected_option.text}\n")
        time.sleep(1)

    select5 = Select(wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#s1'))))
    print(f'✅ 定位到第五个下拉框')
    for index, select in enumerate(select5.options):
        print(f'第{index + 1}个下拉选项'.center(30, '='))
        print(f'选项文本是：{select.text}')
        select5.select_by_value(select.get_attribute('value'))
        print(f"当前选中项：{select5.first_selected_option.text}\n")
        time.sleep(1)

    select6 = Select(wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#testInputEvent'))))
    print(f'✅ 定位到第六个下拉框')
    for index, select in enumerate(select6.options):
        print(f'第{index + 1}个下拉选项'.center(30, '='))
        print(f'选项文本是：{select.text}')
        select6.select_by_visible_text(select.text)
        print(f"当前选中项：{select6.first_selected_option.text}\n")
        time.sleep(1)

except Exception as e:
    print(f'❌ 脚本执行错误'.center(30,'='))
    print(f'错误信息是：',e)

finally:
    browser.quit()
    print(f'✅ 脚本执行完毕，退出浏览器')

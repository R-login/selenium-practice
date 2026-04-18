#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/7 09:58

from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()

browser.get('http://www.baidu.com')
browser.maximize_window()
# browser.set_window_size(100, 768)
import time
# browser.back()
# browser.forward()
# browser.refresh()
# link = browser.find_element(By.LINK_TEXT, '新闻')

# y = browser.find_elements(By.TAG_NAME,"textarea")
# for index,item in enumerate(y):
#     print(index,item.get_attribute("data-ai-placeholder"))
#     if  item.get_attribute("class") == 'chat-input-textarea chat-input-scroll-style':
#         item.send_keys("test1")
# time.sleep(10)
# for index, element in enumerate(y):
#     print(f"===== 第 {index+1} 个 textarea =====")
#     print(f"id: {element.get_attribute('id') or '【无】'}")
#     print(f"class: {element.get_attribute('class') or '【无】'}")
#     print(f"placeholder: {element.get_attribute('placeholder') or '【无】'}")
#     print(f"是否可见: {element.is_displayed() or '【无】'}")  # 区分可见/隐藏元素
#     # print(f"当前输入内容: {element.get_attribute('value')}")
#     print(f"data-ai-placeholder:{element.get_attribute('data-ai-placeholder') or '【无】'}")
#     print(element.get_attribute("随便写一个不存在的属性"))
# y = browser.find_elements(By.TAG_NAME,"a")
# for index,item in enumerate(y):
#     print(f'{index + 1:<2d} -> {item.text or "【无文本】"}')
# browser.find_element(By.PARTIAL_LINK_TEXT,"新").click()
# browser.find_elements(By.CSS_SELECTOR,"textarea")[2].send_keys('111')
# for index,item in enumerate(browser.find_elements(By.XPATH,"//textarea[1]")):
#     print(f"我的下标是{index + 1:<2d} -> {item.get_attribute('placeholder') or '【无文本】'}")
#     if item.get_attribute('placeholder'):
#         item.send_keys('111')
#         time.sleep(5)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(browser,10)
wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'backgroundImage')))
iframe = browser.find_elements(By.CSS_SELECTOR, 'iframe')
print(f'页面上的iframe总数：{len(iframe)}')
# browser.switch_to.iframe(iframe[0])
# print(len(iframe))


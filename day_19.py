#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/13 09:36
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
browser = webdriver.Chrome()
browser.get('https://demo.guru99.com/test/')
browser.maximize_window()
timeout = 10
try:
    wait = WebDriverWait(browser, timeout)
    date_ele = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'[type="datetime-local"]')))
    print(f"name属性：{date_ele.get_attribute('name')}")
    print(f'初始化value的属性：{date_ele.get_attribute("value") or "【无】"}')
    target_date = '2026-04-13T12:00'
    js_input_value = f"arguments[0].value = '{target_date}'"
    browser.execute_script(js_input_value, date_ele)
    time.sleep(3)
    print(f'当前value的属性：{date_ele.get_attribute("value") or "【无】"}')
    print(f'✅ js代码注入成功,赋值：{target_date}')
    actual_value = date_ele.get_attribute("value")
    print(f'实际页面上的value：{actual_value}')
    print(f'目标value和页面实际value比对{target_date == actual_value} ')
    browser.find_element(By.CSS_SELECTOR,"[type='submit']").click()
    # print(f'✅ 已填入新日期：{date_ele.}')
    time.sleep(5)

except Exception as e:
    print(f'❌ 脚本错误'.center(30,'='))
    print('错误信息：',e)

finally:
    browser.quit()
    print(f'✅ 脚本执行完毕，退出浏览器')
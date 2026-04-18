#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/13 13:51
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
browser = webdriver.Chrome()
browser.get("https://ant-design.antgroup.com/components/date-picker-cn")
timeout = 5
try:
    wait = WebDriverWait(browser, timeout)
    date_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"input[placeholder='请选择日期'][disabled]"))
    )
    print(f'初始化日期：{date_input.get_attribute("value")}')
    print(f'当前disabled：{date_input.get_attribute("disabled")}')
    js_remove_ele = "arguments[0].removeAttribute('disabled')"
    browser.execute_script(js_remove_ele,date_input)
    print(f'注入js后的disabled：{date_input.get_attribute("disabled")}')
    date_input.clear()
    # date_input.send_keys('2026-04-13')
    js_input_value = 'arguments[0].value = "2026-04-13"'
    browser.execute_script(js_input_value,date_input)
    print(f'输入value后的值：{date_input.get_attribute("value")}')
    time.sleep(5)



except Exception as e:
    print(f'❌ 脚本错误'.center(30,'='))
    print(f'错误信息：',e)

finally:
    browser.quit()
    print(f'✅ 脚本执行成功，退出浏览器')

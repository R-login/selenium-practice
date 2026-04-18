#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/10 18:44
from asyncio import wait

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
browser = webdriver.Chrome()
try:
    browser.get('https://the-internet.herokuapp.com/checkboxes')
    wait = WebDriverWait(browser,5)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"""[type="checkbox"]""")))
    check_boxs = browser.find_elements(By.CSS_SELECTOR,'[type="checkbox"]')
    print(f"✅ 成功把选择框都装入到列表中")
    for index,check_box in enumerate(check_boxs,start=1):
        print(f'第{index}个选择框的选中状态是{check_box.is_selected()}')
        if  check_box.is_selected():
            print(f"{check_box.get_attribute('checked')}")
            check_box.click()
            print(f"{check_box.get_attribute('checked')}")
            print(f"{type(check_box.get_attribute('checked'))}")
            print(f"✅ 取消已选中的第{index}个选择框")
            time.sleep(3)

except Exception as e:
    print(f"❌ 脚本执行错误".center(20,'='))
    print(f'错误信息{str(e)}')

finally:
    browser.quit()
    print(f'✅ 脚本执行完毕，退出浏览器')
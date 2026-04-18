#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/14 15:33
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/14 10:43
from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import time
import os
from pprint import pprint
browser = webdriver.Chrome()
browser.get("https://redmine.coolkit.cn/login?back_url=https%3A%2F%2Fredmine.coolkit.cn%2Fmy%2Fpage")
browser.maximize_window()
timeout = 5
try:
    wait = WebDriverWait(browser, timeout)
    username_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#username')))
    print(f'✅ 定位到账号输入框，开始输入账号...')
    username_input.send_keys('renyuqiao')
    print(f"✅ 账号输入成功：{username_input.get_attribute('value')}")
    passwd_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#password')))
    print(f"✅ 定位到密码输入框，开始输入密码...")
    passwd_input.send_keys('renyuqiao3333')
    print(f"✅ 密码输入成功：{passwd_input.get_attribute('value')}")
    login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#login-submit')))
    login_button.click()
    print(f'✅ 登录成功')
    table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class = "list issues odd-even sort-by-updated-on sort-desc"]')))
    print(f'✅ 定位到表的元素对象,开始搬运 ⬇️')
    Desk_path = os.path.join(os.path.expanduser('~'),"Desktop")
    file_path = os.path.join(Desk_path,'搬运')
    if os.path.exists(file_path):
        print(f"✅ 桌面存在文件：{file_path}")
    else:
        print(f"❌ 桌面不存在文件：{file_path}")
    thead_tr_th = table.find_elements(By.CSS_SELECTOR,'thead>tr>th')[1:-1]
    thead_list = []
    all_list = []
    with open(file_path,'w',encoding='utf-8') as f:
        for th in thead_tr_th:
            thead_list.append(th.text)

        print(f'✅ 文件创建成功{file_path}')
        tbody_tr = table.find_elements(By.CSS_SELECTOR,'tbody>tr')
        tbody_list = []

        for tr in tbody_tr:
            tds = tr.find_elements(By.CSS_SELECTOR,'tbody>tr>td')[1:-1]
            for index,td in enumerate(tds):
                tbody_list.append(td.text)
            pprint(dict(zip(thead_list, tbody_list)))
            print()












except Exception as e:
    print(f'❌ 脚本执行错误'.center(100,'='))
    print(f'错误信息：',e)


finally:
    browser.quit()
    print(f'✅ 脚本执行完毕，退出浏览器')

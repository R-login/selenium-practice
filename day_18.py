#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/12 16:27
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
browser = webdriver.Chrome()
browser.get('https://www.selenium.dev/selenium/web/web-form.html')
browser.maximize_window()
file_path = r"C:\Users\15123\Desktop\30adcd40c50c4ef08880251c27b8d74a.png"
try:
    wait = WebDriverWait(browser,10)
    if not os.path.exists(file_path):
        raise FileExistsError(f'❌ 上传路径不存在:{file_path}')
    file_name = os.path.basename(file_path)
    print(f'📖 文件名称是{file_name}')
    print(f'✅ 校验文件成功：{file_name}')
    up_load = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"[type='file']")))
    print(f'type属性是：{up_load.get_attribute("type")}')
    print(f'文本属性是：{up_load.text or "【无文本】"}')
    print(f'✅ 成功定位到上传文件的按钮')
    up_load.send_keys(file_path)
    print(f'✅ 已提交上传指令')
    wait.until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR,"[type='file']"),file_name))
    print(f'✅ 上传成功，页面已确认接收文件{file_name}')
    time.sleep(5)
except Exception as e:
    print(f'❌ 脚本错误'.center(30,'='))
    print(f'错误详情：{str(e)}')
    raise #
finally:
    browser.quit()
    print(f'✅ 脚本执行完毕，退出浏览器')
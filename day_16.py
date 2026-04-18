#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/10 09:44


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
try:
    browser.get(r"file:///C:\Users\15123\Desktop\alert.text.html.html")
    import time
    time.sleep(2)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, """[onclick="alert('我是alert')"]""")))
    print(f'✅ 定位到第一个按钮')
    browser.find_element(By.CSS_SELECTOR,"""[onclick="alert('我是alert')"]""").click()
    print('✅ 成功点击第一个按钮')
    time.sleep(1)
    alert = browser.switch_to.alert
    print(f'✅ 第一个按钮的文本是 -> {alert.text}')
    time.sleep(1)
    alert.accept()
    print(f'✅ 点击确定成功')
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"""[onclick="confirm('我是confirm')"]""")))
    print(f"✅ 定位到第二个按钮")
    browser.find_element(By.CSS_SELECTOR,"""[onclick="confirm('我是confirm')"]""").click()
    print(f"✅ 成功点击第二个按钮")
    time.sleep(1)
    alert_confirm = browser.switch_to.alert
    print(f'这是第二个弹窗的文本 -> {alert_confirm.text}')
    alert_confirm.dismiss()
    print(f'✅ 成功取消第二个按钮')
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, """[onclick="let res = prompt('我是prompt','请输入'); alert('你输入的是：' + res)"]""")))
    print(f"✅ 成功定位第四个按钮")
    browser.find_element(By.CSS_SELECTOR, """[onclick="let res = prompt('我是prompt','请输入'); alert('你输入的是：' + res)"]""").click()
    print(f"✅ 成功点击第四个按钮")
    time.sleep(1)
    alert_04 = browser.switch_to.alert
    print(f"这是第四个弹窗的文本 -> {alert_04.text}")
    alert_04.send_keys('✅ 成功输入')
    print(f'✅ 输入成功')
    time.sleep(3)
    alert_04.accept()
    print(f'✅ 成功点击确定')
    time.sleep(3)

except Exception as e:
    print(f'❌ 脚本执行错误{str(e)}')

finally:
    print(f'✅ 脚本执行完毕，关闭浏览器')
    browser.quit()
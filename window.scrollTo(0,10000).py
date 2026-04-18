#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/16 17:23
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



browser = webdriver.Chrome()
browser.get("https://2captcha.com/demo/normal")
wait = WebDriverWait(browser, 10)

for i in range(0,10000,500):
    browser.execute_script(f"window.scrollTo(0,{i})")
    time.sleep(0.5)
    button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a._buttonPrimary_1qfxa_40")))
    if button:
        browser.execute_script("arguments[0].click()",button)
        break
time.sleep(2)
print(f'当前浏览器title：{browser.title}')
print(f'当前浏览器url：{browser.current_url}')

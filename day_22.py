#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/16 10:11
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
browser.get("https://2captcha.com/demo/normal")
img = browser.find_element(By.CSS_SELECTOR, "img._captchaImage_rrn3u_9").screenshot_as_png
import ddddocr
def png(tupian):
    ocr = ddddocr.DdddOcr()
    chulihaole = ocr.classification(tupian)
    print(f"当前浏览器标题：{browser.title}")
    print(f"当前url:：{browser.current_url}")
    return chulihaole

tupian_str = png(img)
wait = WebDriverWait(browser, 10)
try:
    browser.find_element(By.CSS_SELECTOR, "input._inputInner_ws73z_12").send_keys(tupian_str)

    ele = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']")))
    browser.execute_script("arguments[0].click()", ele)
    suc = EC.visibility_of_element_located((By.CSS_SELECTOR,"._successMessage_rrn3u_1"))
    err = EC.visibility_of_element_located((By.CSS_SELECTOR,"._alertBody_14gi4_16"))
    result = wait.until(
             EC.any_of(suc,
                  err
        )
    )
    if result.get_attribute("class") in "._successMessage_rrn3u_1":
        print(f'✅ 提示信息：{result.text}')
    else:
        print(f'❌ 提示信息：{result.text}')


except Exception as e:
    print(f"❌ 其他错误信息：",e)

finally:
    print(f'✅ 脚本执行结束，关闭浏览器')
    browser.quit()



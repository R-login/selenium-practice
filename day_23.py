#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/17 13:58
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
browser.implicitly_wait(5)
browser.find_element(By.LINK_TEXT,"贴吧").click()
def jubin(*,jubin_title_url,screenshot_on_fail=True):
    all_handle = browser.window_handles
    for handle in all_handle:
        browser.switch_to.window(handle)
        if jubin_title_url in browser.title or jubin_title_url in browser.current_url:
            print(f"✅ 成功切换到目标句柄，当前标题：{browser.title}")
            print(f'当前url -> {browser.current_url}')
            return True

    if screenshot_on_fail:
        save_dir = "screenshot"
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)

        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
        screenshot_name = f"句柄切换失败_{timestamp}.png"
        screenshot_dir = os.path.join(save_dir, screenshot_name)
        browser.save_screenshot(screenshot_dir)
        print(f"📷 失败截图已保存{screenshot_name}")

        print(f"😭 切换句柄失败，当前标题：{browser.title}")
    return False


print(jubin(jubin_title_url=""))
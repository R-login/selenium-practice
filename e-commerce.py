#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/20 14:16
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time,os
browser = webdriver.Chrome()
browser.get("https://www.saucedemo.com/")
browser.maximize_window()
action = webdriver.ActionChains(browser)
download_dir = r"C:\selenium - practice\saucedemo_downloads"
os.makedirs(download_dir,exist_ok=True)


try:
    #登录页 - 鼠标登录
    username_input = WebDriverWait(browser,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#user-name")))
    username_input.send_keys("standard_user")
    password_input = WebDriverWait(browser,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#password")))
    password_input.send_keys("secret_sauce")
    submit = WebDriverWait(browser,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#login-button")))
    submit.click()
    print(f'✅ 登录成功')

    #商品页筛选 - 通过下标选择第二个首字母倒叙显示
    sel = Select(WebDriverWait(browser,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".product_sort_container"))))
    sel.select_by_index(1)
    sel_new = Select(WebDriverWait(browser,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".product_sort_container"))))
    print(f"✅ 通过下标选择第二个首字母倒叙显示:{sel_new.first_selected_option.text}")

    #商品页筛选 - 通过value选择第三个价格倒叙显示
    sel_new.select_by_value("lohi")
    sel_new_new = Select(WebDriverWait(browser,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".product_sort_container"))))
    print(f"✅ 通过value选择第三个价格倒叙显示:{sel_new_new.first_selected_option.text}")

    # 商品页筛选 - 通过文本选择第四个价格正叙显示
    sel_new_new.select_by_visible_text("Price (high to low)")
    sel_new_new_new = Select(WebDriverWait(browser,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".product_sort_container"))))
    print(f'✅ 通过文本选择第四个价格正叙显示:{sel_new_new_new.first_selected_option.text}')

    #鼠标悬停第一个商品名字上
    ele = WebDriverWait(browser,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".inventory_item_name ")))
    action.move_to_element(ele).perform()
    print(f"✅ 鼠标悬停到第一个商品名上")

    #使用键盘上下滑动
    action.send_keys(Keys.UP).perform()
    action.send_keys(Keys.PAGE_DOWN).perform()
    print(f"✅ 鼠标上下滑动")

    #点击增加商品 - 截图并下载订单文本到指定文件
    screenshot = "order_screenshot.png"
    browser.save_screenshot(os.path.join(download_dir,screenshot))
    browser.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack").click()
    order_name = browser.find_elements(By.CSS_SELECTOR,".inventory_item_name")
    with open(os.path.join(download_dir,"order_download.txt"),"w",encoding="utf-8") as f:
        f.write("商品订单文本".center(50,"=")+"\n")
        for index,item in enumerate(order_name,1):
            f.write(f"第{index}个商品文本 -> {item.text}"+"\n")
        print(f"✅ 商品订单文本下载完毕")





except Exception as e:
    print(f'❌ 脚本执行错误'.center(30,"="))
    print(f'错误信息：',e)

finally:
    browser.quit()
    print(f"✅ 脚本执行完毕，退出浏览器")



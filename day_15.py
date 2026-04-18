#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/4/9 09:25
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
try:
    browser.get('https://www.runoob.com/try/try.php?filename=tryjs_alert')
    browser.maximize_window()
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    wait = WebDriverWait(browser,5)
    # wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'iframe')))
    # iframes = browser.find_elements(By.CSS_SELECTOR, 'iframe')
    # iframe = browser.switch_to.frame("iframeu6752627_0")
    # print(type(iframe))
    # print(iframe)
    # print(iframes[1].get_attribute('frameborder'))
    # for index, iframe in enumerate(iframes):
    #     # print(f'第{index + 1}个iframe'.center(20,'*'))
    #     # print(f"iframe的id是{iframe.get_attribute('id') or '【无】'}")
    #     # print(f"iframe的name是{iframe.get_attribute('name') or '【无】'}")
    #     # print(f"iframe的scr是{iframe.get_attribute('src')[:50] or '【无】'}")
    #     # print(f"iframe的frameborder是{iframe.get_attribute('frameborder') or '【无】'}")
    #     # print(f"iframe的width是{iframe.get_attribute('width') or '【无】'}")
    #     # print(f"iframe的height是{iframe.get_attribute('height') or '【无】'}")
    #     # print(f"iframe的scrolling是{iframe.get_attribute('scrolling') or '【无】'}")
    #     if iframe.get_attribute('id') == 'iframeu6752627_0':
    #         print(index + 1)
    #         browser.switch_to.frame('iframeu6752627_0')
    #         break
    iframes = browser.find_elements(By.CSS_SELECTOR, 'iframe')
    try:
        for index,iframe in enumerate(iframes):
            print(f'第{index + 1}个iframe'.center(20,'='))
            print(f"frameborder:{iframe.get_attribute('frameborder') or '【无frameborder】'}")
            print(f"id:{iframe.get_attribute('id') or '【id】'}")
            print(f"title:{iframe.get_attribute('title') or '【title】'}")
            if iframe.get_attribute('id') == 'iframeResult':
                print(f"✅ 找到iframe，正在切入")
                browser.switch_to.frame(iframe)
                print(f'✅ 已成功切入iframe')
                break

    except Exception as e:
        print(f'❌ {str(e)}')

    try:
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input')))
        print(f'✅ 定位到了“显示警告框”按钮，当前可点击')
        browser.find_element(By.CSS_SELECTOR,'input').click()
        print(f'✅ 点击到了‘显示警告框’按钮')
        import time
        time.sleep(3)

    except Exception as e:
        print(f'❌ {str(e)}')

    alert = browser.switch_to.alert
    try:
        print(f"✅ 尝试打印alert弹窗的文本：{alert.text}")
        alert.accept()
        print(f'✅ 点击到了弹窗的确定')
        time.sleep(5)

    except Exception as e:
        print(f'❌ 脚本执行错误：{str(e)}')

except Exception as e:
    print(f'❌ 脚本执行错误：{str(e)}')

finally:
    browser.quit()






from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)


# 1. 手动登录+保存Cookie（只跑一次）
def manual_login_save_cookie():
    browser.get("https://redmine.coolkit.cn/login")
    input("请手动登录Redmine，登录成功后按回车键继续...")

    cookies = browser.get_cookies()
    with open("redmine_cookies.json", "w", encoding="utf-8") as f:
        json.dump(cookies, f, ensure_ascii=False, indent=2)
    print("✅ Cookie 已保存！")
    browser.quit()


# 2. 免登录（以后永远用这个）
def auto_login_with_cookie():
    browser.get("https://redmine.coolkit.cn/")
    time.sleep(1)

    with open("redmine_cookies.json", "r", encoding="utf-8") as f:
        cookies = json.load(f)

    for cookie in cookies:
        cookie.pop("sameSite", None)
        cookie.pop("expiry", None)
        cookie.pop("storeId", None)
        browser.add_cookie(cookie)

    browser.refresh()
    browser.get("https://redmine.coolkit.cn/my/page")

    try:
        wait.until(EC.title_contains("我的工作台"))
        print("✅ 免登录成功！已进入Redmine工作台")
        print("当前URL：", browser.current_url)
    except Exception as e:
        print("❌ 登录失败，当前页面：", browser.title)
        print("当前URL：", browser.current_url)

    time.sleep(5)
    browser.quit()


# 第一次运行：执行manual_login_save_cookie()
# manual_login_save_cookie()

# 后续运行：执行auto_login_with_cookie()
auto_login_with_cookie()
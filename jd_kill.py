# 导入要使用到的模块(工具)
import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import win32com.client
from selenium.webdriver.support.wait import WebDriverWait

speaker = win32com.client.Dispatch("SAPI.SpVoice")

# 秒杀时间 算盘--软件 browser=浏览器
times = '2023-08-27 18:33:00'
# 打开浏览器
browser = webdriver.Chrome()

# 进入京东网页
browser.get("https://www.jd.com/")
time.sleep(3)
# 扫码登录
browser.find_element(By.LINK_TEXT, "你好，请登录").click()
print(f"请扫码")

browser.find_element(By.LINK_TEXT, "扫码登录").click()

wait = WebDriverWait(browser, 300)

target_string = "驿路惊鸿"

found = False

while not found:
    try:
        # 查找页面上的元素\
        print("开始查找字符串")
        element = browser.find_element(By.LINK_TEXT, target_string)
        print("目标字符串已找到：", target_string)
        found = True
        break  # 找到目标字符串后跳出循环
    except:
        pass  # 如果找不到元素，继续循环
# 打开购物车页面
browser.get("https://cart.jd.com/cart_index")
time.sleep(5)
'''
1、打开浏览器
2、登录京东账号
3、扫码登录
4、进入购物车
5、选中需要购买的商品
6、对比时间
7、到抢购时间 点击结算按钮
'''

# 全选购物车
# while True:
#     if browser.find_element_by_class_name("jdcheckbox"):
#         browser.find_element_by_class_name("jdcheckbox").click()
#         break

while True:
    # 获取电脑现在的时间
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    # 对比时间，时间到的话就点击结算
    print(now)
    # 判断是不是到了秒杀时间?
    if now > times:
        # 点击结算按钮
        while 1 == 1:
            try:
                if browser.find_element(By.LINK_TEXT, "去结算"):
                    print("here")
                    browser.find_element(By.LINK_TEXT, "去结算").click()
                    print(f"主人,结算提交成功,我已帮你抢到商品啦,请及时支付订单")
                    speaker.Speak(f"主人,结算提交成功,我已帮你抢到商品啦,请及时支付订单")
                    speaker.Speak(f"赵银春，你是个大傻蛋")
                    break
            except:
                pass
        # 点击提交订单按钮
        while True:
            try:
                if browser.find_element(By.LINK_TEXT, "提交订单"):
                    browser.find_element(By.LINK_TEXT, "提交订单").click()
                    print(f"抢购成功，请尽快付款")
            except:
                print(f"主人,我已帮你抢到商品啦,您来支付吧")
                break
        time.sleep(0.01)

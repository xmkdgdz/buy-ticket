import configparser
import sys
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from appium.options.android import UiAutomator2Options


# 模拟下拉刷新
def refresh():
    print("刷新")
    driver.swipe(500, 400, 500, 2000, 300)
    sleep(0.1)


config = configparser.ConfigParser()
config.read("config.ini", encoding="utf-8")
config_name = sys.argv[1]
session = config[config_name]["session"]
price = config[config_name]["price"]

options = UiAutomator2Options().load_capabilities({
    "platformName": "Android",
    "platformVersion": "12",
    "deviceName": "RNA-AL00",
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "noReset": True,
    "newCommandTimeout": 6000,
    # "automationName": "UiAutomator2"
})
driver = webdriver.Remote("http://localhost:4723", options=options)

# sleep(5)

# 设置等待时间
# driver.implicitly_wait(1)

try:
    while True:
        refresh()
        buy_btn = driver.find_element(by=By.ID,
                                      value='cn.damai:id/trade_project_detail_purchase_status_bar_container_fl')
        # 立即购票
        if buy_btn.get_attribute('bounds') == '[501,2500][1203,2647]':
            print("开始购票")
            # 开始购买
            driver.find_element(by=By.XPATH,
                                value='//android.widget.FrameLayout['
                                      '@resource-id="cn.damai:id'
                                      '/trade_project_detail_purchase_status_bar_container_fl"]').click()
            # 场次
            driver.find_element(by=By.XPATH,
                                value=f'(//android.view.ViewGroup[@resource-id="cn.damai:id/item_flowlayout"])[{session}]').click()
            # 票档
            driver.find_element(by=By.XPATH,
                                value=f'(//android.view.ViewGroup[@resource-id="cn.damai:id/item_flowlayout"])[{price}]').click()
            # 有票
            if driver.find_element(by=By.ID, value='cn.damai:id/tv_price'):
                print("有票")
                # 购买
                driver.find_element(by=By.ID, value='cn.damai:id/btn_buy_view').click()
                # 选择人员
                person = driver.find_element(by=By.XPATH, value='//android.widget.CheckBox['
                                                                '@resource-id="cn.damai:id/checkbox"]')
                if person.get_attribute('checked') == 'false':
                    person.click()
                # 立即提交
                driver.find_element(by=By.XPATH, value='//android.widget.TextView[@text="立即提交"]').click()
                if driver.find_element(by=By.ID, value='com.alipay.android.app:id/flybird_user_logo'):
                    print("进入支付界面")
                    break
            # 缺货
            else:
                print("缺货")
                # 退出
                driver.find_element(by=By.ID, value='cn.damai:id/title_back_btn').click()
        else:
            print("未到购票时间")

except KeyboardInterrupt:
    driver.quit()



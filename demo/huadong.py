from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class init_driver():
    # 定义一个参数
    desire_caps = {}
    # 系统
    desire_caps['platformName'] = 'Android'
    # 系统版本
    desire_caps['platforVersion'] = '9'
    # 设备号
    desire_caps['deviceName'] = 'd574beff'
    # 包名
    desire_caps['appPackage'] = 'com.android.settings'
    # 启动名
    desire_caps['appActivity'] = '.HWSettings'
    # 不清数据
    desire_caps['noReset'] = 'True'

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)

    # driver.swipe(253,1237,299,732)
    start_ele = driver.find_element_by_xpath("//*[contains(@text,'应用')]")
    end_ele = driver.find_element_by_xpath("//*[contains(@text,'显示')]")
    time.sleep(2)
    driver.drag_and_drop(start_ele, end_ele)
    time.sleep(5)
    TouchAction(driver).

    driver.quit()

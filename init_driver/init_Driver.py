from appium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait

class init_driver():
    # 定义一个参数
    desire_caps = {}
    # 系统
    desire_caps['platformName'] = 'Android'
    # 系统版本
    desire_caps['platforVersion'] = '7.1.2'
    # 设备号
    desire_caps['deviceName'] = 'emulator-5554'
    # 包名
    desire_caps['appPackage'] = 'com.android.settings'
    # 启动名
    desire_caps['appActivity'] = '.Settings'
    # 不清数据
    desire_caps['noReset'] = 'True'

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)

    # try:
    #     #点击
    #     driver.find_element_by_id("android:id/search_src_text").click()
    #     driver.find_element_by_id("android:id/search_src_text").send_keys("设置")
    #     time.sleep(2)
    #
    #
    #     # # 根据列表定位元素
    #     # ele_list = WebDriverWait(driver,5,0.5).until(lambda x :x.find_elements_by_id("android:id/title"))
    #     # # ele_list = driver.find_elements_by_id("android:id/title")
    #     # for i in ele_list:
    #     #     if i.text == '声音':
    #     #         i.click()
    #     #         break
    #
    # except Exception as e:
    #     print(e)
    # finally:
    #     time.sleep(5)
    #     driver.quit()

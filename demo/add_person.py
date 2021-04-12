from appium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait

class add_per():
    # 定义一个参数
    desire_caps = {}
    # 系统
    desire_caps['platformName'] = 'Android'
    # 系统版本
    desire_caps['platforVersion'] = '9'
    # 设备号
    desire_caps['deviceName'] = 'CLB7N19308001503'
    # 包名
    desire_caps['appPackage'] = 'com.android.contacts'
    # 启动名
    desire_caps['appActivity'] = '.activities.PeopleActivity'
    # 不清数据
    desire_caps['noReset'] = 'True'

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)

    #点击添加按钮
    driver.find_element_by_id("com.android.contacts:id/hw_fab").click()
    time.sleep(2)
    #输入内容
    ele_text_list = driver.find_elements_by_class_name("android.widget.EditText")
    for i in ele_text_list:
        if "姓名" in i.text:
            i.send_keys("高老")
        if "电话号码" in i.text:
            i.send_keys("18812345678")
        if "邮件" in i.text:
            i.send_keys("123456@qq.com")
        if "备注" in i.text:
            i.send_keys("她是高老庄")

    #点击确认
    submit = driver.find_element_by_id("android:id/icon2")
    submit.click()

    time.sleep(5)
    driver.quit()




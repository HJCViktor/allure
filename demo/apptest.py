from appium import webdriver
import time
import base64

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
desire_caps['appActivity'] = '.MainSettings'
# 不清数据
desire_caps['noReset'] = 'True'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)

# 关闭app
# driver.close_app()

# 安装
# driver.install_app("F:/弱网工具.apk")

# 卸载
# driver.remove_app("com.tencent.qnet")

# print(driver.is_app_installed("com.tencent.qnet"))
# print(driver.is_app_installed("com.gzyct.yctwallet"))
#
# if driver.is_app_installed("com.tencent.qnet"):
#     driver.remove_app("com.tencent.qnet")
# else:
#     driver.install_app("F:/弱网工具.apk")

# 将哈哈哈写入haha.txt文件
# data = str(base64.b64encode("哈哈哈".encode("utf-8")),"utf-8")
# driver.push_file("/sdcard/haha.txt",data)

# 拉去手机中文件
# data=driver.pull_file("/sdcard/haha.txt")
# print(str(base64.b64decode(data),"utf-8"))
# 退出手机驱动对象d

current_page_data = driver.page_source
for i in ("双卡","显示"):
    if i in current_page_data:
        print(True)
    else:
        print(False)
driver.quit()

from init_driver.init_Driver import init_driver
import os
import base64


def push(tag, pc_path, phone_path):
    # tag==1:adb /tag==2:appium
    if tag == "1":
        os.system("adb push %s %s" % (pc_path, phone_path))
    if tag == "2":
        driver = init_driver()
        with open(pc_path, "r") as f:
            data = str(base64.b64encode(f.read().encode("utf-8")), "utf-8")
            driver.push_file(phone_path, data)


if __name__ == '__main__':
    push(1, "F:/gat脚本.txt", "/sdcard/gat脚本1243.txt")
    # push("2","F:/gat脚本.txt", "/sdcard/gat脚本123.txt")

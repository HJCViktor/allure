import pytest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Test_index:
    def setup_class(self):
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
        # 启动
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)

    def teardown_class(self):
        self.driver.quit()

    def wait_element(self, type, data):
        if type == 'id':
            return WebDriverWait(self.driver, 5, 0.5).until(lambda x: x.find_element_by_id(data))
        if type == 'xpath':
            return WebDriverWait(self.driver, 5, 0.5).until(lambda x: x.find_element_by_xpath(data))

    @pytest.fixture()
    def in_index(self):
        # 声音
        sing = self.wait_element("xpath", "//*[contains(@text,'声音')]")
        # 更多
        yidonshuju = self.wait_element("xpath", "//*[contains(@text,'移动数据')]")
        # 滑动，看见位置信息
        self.driver.drag_and_drop(sing, yidonshuju)
        # 点击位置信息
        self.wait_element("xpath", "//*[contains(@text,'位置信息')]").click()

    @pytest.mark.usefixtures("in_index")
    def test_demo(self):
        #模式text
        mo_id = self.wait_element("id","android:id/summary")
        # 点击模式
        moshi = self.wait_element("xpath", "//*[contains(@text,'模式')]").click()
        # 选择低耗电量
        dihao = self.wait_element("xpath", "//*[contains(@text,'低耗电量')]").click()
        #返回
        self.driver.keyevent(4)
        #断言
        assert "低耗电量" in mo_id.text



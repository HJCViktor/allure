import pytest,allure


class Test_ABC:
    @allure.step(title="第一个测试")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_a_001(self):
        allure.attach(name="这是一个描述",body="是是")
        assert 1==0

    @allure.step(title="第二个测试")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_a_002(self):
        allure.attach(name="这是二个描述", body="是是")
        assert 1 == 0



import pytest

class Test_ABC:

    @pytest.mark.run(order=1)
    def test_a(self):
        print(">>>>aaa")
        assert True

    @pytest.mark.run(order=3)
    def test_b(self):
        print(">>>>bbb")
        assert 3==1

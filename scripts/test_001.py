import pytest, allure

class Test_abc:
    @allure.step("第一个测试步骤")
    def test_001(self):
        assert 1


# if __name__ == '__main__':
#     pytest.main(['-s','-q','--alluredir','./report','test_001.py'])
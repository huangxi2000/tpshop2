import os
import sys
sys.path.append(os.getcwd())
import pytest

from base.read_yaml import ReadYaml

from base.get_driver import get_driver
from page.page_in import PageIn


def get_data():
    res = ReadYaml("data_login.yaml").read_yaml()
    list1 = []
    for data in res.values():
        list1.append((data.get("username"), data.get("password"), data.get("code")))
    return list1

# 登录测试
class TestLogin():
    def setup(self):
        self.driver = get_driver()
        self.page = PageIn(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("username, password, code", get_data())
    def test_login(self, username, password, code):
        main = self.page.page_in_pagemain()
        main.open_url()
        login = self.page.page_in_pagelogin()
        # 点击首页登录
        main.page_main_login_click()
        # 登录页面输入
        login.page_login_username(username)
        login.page_login_password(password)
        login.page_login_code(code)
        login.page_login_btn()
        


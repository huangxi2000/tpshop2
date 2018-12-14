import os
import sys

import pytest

sys.path.append(os.getcwd())


from base.get_driver import get_driver
from page.page_in import PageIn


# 登录测试
class TestLogin():
    def setup_class(self):
        self.driver = get_driver()
        self.page = PageIn(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("username, password, code", [("18612345678", "123456", "8888")])
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


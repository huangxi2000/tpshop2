from page.page_login import PageLogin
from page.page_main import PageMain


class PageIn():
    def __init__(self, driver):
        self.driver = driver

    # 创建登录页面实例化对象
    def page_in_pagelogin(self):
        return PageLogin(self.driver)

    # 创建首页实例化对象
    def page_in_pagemain(self):
        return PageMain(self.driver)
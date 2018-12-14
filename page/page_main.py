import page
from base.base import Base


class PageMain(Base):

    def open_url(self):
        self.driver.get("http://www.tpshop.com/")

    # 首页点击登录
    def page_main_login_click(self):
        self.base_click(page.main_login_btn)

import page
from base.base import Base


# 登录页面
class PageLogin(Base):
    # 输入帐号
    def page_login_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_login_password(self, password):
        self.base_input(page.login_password, password)

    # 输入验证码
    def page_login_code(self, code):
        self.base_input(page.login_code, code)

    # 点击登录
    def page_login_btn(self):
        self.base_click(page.login_btn)

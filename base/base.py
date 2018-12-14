from selenium.webdriver.support.wait import WebDriverWait


class Base():
    # 实例化driver对象,方便调用
    def __init__(self, driver):
        self.driver = driver

    # 封装 找元素方法
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 封装点击
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 封装输入
    def base_input(self, loc, value):
        ele = self.base_find_element(loc)
        # 清空
        ele.clear()
        # 输入
        ele.send_keys(value)
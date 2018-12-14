from selenium.webdriver.common.by import By


""" 以下为主页登录相关配置 """
main_login_btn = By.XPATH, "//*[@class='red']"


""" 以下为登录页面相关配置 """
login_username = By.ID, "username"
login_password = By.ID, "password"
login_code = By.ID, "verify_code"
login_btn = By.NAME, "sbtbutton"
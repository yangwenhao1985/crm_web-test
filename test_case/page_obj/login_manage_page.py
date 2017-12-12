from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from test_case.page_obj.base import Page


class LoginManagePage(Page):

    username_loc = (By.XPATH, "//input[@placeholder='请输入手机号']")
    pwd_loc = (By.XPATH, "//input[@placeholder='密码']")
    login_btn = (By.XPATH, "//input[@value='登录']")
    hello_text_loc = (By.XPATH, "//li[@class='hello']/a")
    fail_text_loc = (By.XPATH, "//div[@class='key']/span")
    logout_loc = (By.XPATH, "//li[@class='out']/img")
    logout_btn_loc = (By.XPATH, "//p[@class='logout']")

    # 用户登录
    def user_login(self, username, pwd):
        self.open_url()
        time.sleep(2)
        self.type_username(username)
        time.sleep(2)
        self.type_pwd(pwd)
        time.sleep(2)
        self.click_login_btn()
        time.sleep(2)

    # 点击登录按钮
    def click_login_btn(self):
        self.click(*self.login_btn)

    # 输入账号
    def type_username(self, username):
        self.type_text(username, *self.username_loc)

    # 输入密码
    def type_pwd(self, pwd):
        self.type_text(pwd, *self.pwd_loc)

    # 获取登录成功后，右上角显示的欢迎文案，用于判断是否登录成功
    def get_hello_text(self):
        return self.get_text(*self.hello_text_loc)

    # 获取登陆失败提示文案
    def get_fail_text(self):
        return self.get_text(*self.fail_text_loc)

    def move_logout(self):
        act1 = ActionChains(self.driver)
        ele = self.find_element(*self.logout_loc)
        act1.move_to_element(ele).perform()

    def user_logout(self):
        self.move_logout()
        time.sleep(1)
        self.click(*self.logout_btn_loc)
        time.sleep(2)

if __name__ == '__main__':
    pass

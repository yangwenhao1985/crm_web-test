import unittest
import time
from parameterized import parameterized
from test_case.models.function import read_excel
from test_case.models.function import screen_shot
from test_case.page_obj.login_manage_page import LoginManagePage
from test_case.models.MyUnit import MyLoginTest


class LoginTestCase(MyLoginTest):
    """ 用户登录测试类 """

    @parameterized.expand(input=read_excel('user', 'user_login'))
    def test_login(self, phone, username, pwd, expect_value):
        """
        用户登录测试用例。
        :param phone: 用户手机号
        :param username: 用户姓名
        :param pwd: 用户密码
        :param expect_value: 预期值
        :return:
        """
        self.lg_page = LoginManagePage(self.driver, self.url)
        time.sleep(2)
        self.lg_page.type_username(phone)
        time.sleep(1)
        self.lg_page.type_pwd(pwd)
        time.sleep(2)
        self.lg_page.click_login_btn()
        time.sleep(1)
        screen_shot(self.driver, '登录.png')
        if self.lg_page.get_title() == "欢迎":
            time.sleep(2)
            success_txt = self.lg_page.get_hello_text()
            self.assertIn(username, success_txt)
        else:
            fail_txt = self.lg_page.get_fail_text()
            self.assertEqual(fail_txt, expect_value)

    @parameterized.expand(input=read_excel('user', 'user_logout'))
    def test_logout(self, phone, pwd):
        self.lg_page = LoginManagePage(self.driver, self.url)
        time.sleep(2)
        self.lg_page.user_login(phone, pwd)
        time.sleep(3)
        if self.lg_page.get_title() == 'Login':
            self.fail("该用户登录失败，请检查测试数据！")
        else:
            self.lg_page.user_logout()
            time.sleep(2)
            screen_shot(self.driver, '退出登录.png')
            self.assertEqual('Login', self.lg_page.get_title())


if __name__ == '__main__':
    unittest.main()

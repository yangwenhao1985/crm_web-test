import time
import unittest
from parameterized import parameterized
from test_case.models.MyUnit import MyTestOne
from test_case.models.function import read_excel
from test_case.page_obj.user_manage_page import UserManagePage
from test_case.page_obj.login_manage_page import LoginManagePage
from test_case.models.function import screen_shot

"""
@FileName: 学员管理测试类
@Author:Sixmiaomiao
@Create on: 2017-06-14
@Update on: 2017-09-20
@Update by: Sixmiaomiao
"""


class UserManageTestCase(MyTestOne):
    """ 账号管理测试类 """

    # @parameterized.expand(input=read_excel('user', 'add_user'))
    # def test_add_user(self, operator_phone, operator_name, name, phone, web_chat, dept, role, sup, level, sex, email, pic, expect):
    #     """ 添加账号测试用例 """
    #
    #     self.user_page.change_user(operator_phone, operator_name)
    #     time.sleep(2)
    #     self.user_page.click_add_user_menu()  # 点击添加账号菜单
    #     time.sleep(2)
    #     self.user_page.type_user_name(name)  # 输入用户姓名
    #     self.user_page.type_user_phone(phone)  # 输入用户电话
    #     self.user_page.type_webchat(web_chat)  # 输入微信号
    #     self.user_page.sel_dept(dept)  # 选择部门
    #     time.sleep(2)
    #     self.user_page.sel_role(role)  # 选择岗位
    #     time.sleep(2)
    #     self.user_page.sel_superior(sup)  # 选择上级
    #     self.user_page.sel_user_level(level)  # 选择职级
    #     self.user_page.sel_sex(sex)  # 选择性别
    #     self.user_page.type_email(email)  # 输入邮箱
    #     self.user_page.upload_pic(pic)  # 上传头像
    #     time.sleep(2)
    #     self.user_page.click_save_btn()  # 点击保存
    #     time.sleep(2)
    #     actual_value = self.user_page.get_pop_text()
    #     self.assertEqual(expect, actual_value, msg="实际结果与预期结果不一致，请查看！")

    @parameterized.expand(input=read_excel('user', 'edit_user'))
    def test_edit_user(self, operator_phone, operator_name, new_name,
                       old_phone, new_phone, new_webchat, new_email, expect):
        """
        编辑用户功能测试用例。
        :param operator_phone: 操作者手机号
        :param operator_name: 操作者名称
        :param new_name: 新名称
        :param old_phone: 原名称
        :param new_phone: 新手机号
        :param new_webchat: 新微信号
        :param new_email: 新邮箱
        :param expect: 预期值
        :return: None
        """

        self.user_page.change_user(operator_phone, operator_name)  # 切换用户
        time.sleep(2)
        self.user_page.click_user_list_menu()  # 点击账号列表菜单
        time.sleep(2)
        self.user_page.query_by_name_or_phone(old_phone)  # 通过原手机号查询用户
        time.sleep(2)
        result_num = self.user_page.get_query_result_list_num()
        if result_num and result_num == 1:  # 判断结果列表不为空且只有1条数据，如果存在则编辑该用户
            self.user_page.click_edit_btn()  # 点击编辑按钮
            time.sleep(2)
            self.user_page.switch_window()  # 切换窗口
            time.sleep(2)
            self.user_page.type_user_name(new_name)  # 输入用户姓名
            self.user_page.type_user_phone(new_phone)  # 输入用户电话
            self.user_page.type_webchat(new_webchat)  # 输入微信
            self.user_page.type_email(new_email)  # 输入邮箱
            self.user_page.click_save_btn()  # 点击保存按钮
            time.sleep(1)
            actual_value = self.user_page.get_pop_text()  # 获取保存后弹出窗口的文案
            screen_shot(self.driver, "编辑用户.png")  # 截图
            self.assertEqual(expect, actual_value, msg="实际结果与预期结果不一致，请查看！")  # 断言弹窗文案是否一致
            self.assertEqual(new_phone, self.user_page.get_phone_value())  # 断言修改后手机号是否与新手机号一致
        else:
            screen_shot(self.driver, "编辑用户-用户列表.png")  # 截图
            self.fail("用户列表为空或数据不唯一，请检查测试数据！")  # 结果列表为空，则报失败

    @parameterized.expand(input=read_excel('user', 'query_user'))
    def test_query_user(self, operator_phone, operator_name, company, usr, role):
        """
         用户查询测试用例 。
        :param operator_phone: 操作者手机号
        :param operator_name: 操作者名称
        :param company: 公司名称
        :param usr: 用户手机号或姓名
        :param role: 角色
        :return: None
        """

        self.user_page.change_user(operator_phone, operator_name)  # 切换用户
        time.sleep(2)
        self.user_page.click_user_list_menu()  # 点击账号列表菜单
        time.sleep(2)
        if company:  # 如果测试数据给了公司名称，则选择公司
            self.user_page.sel_query_company(company)
        self.user_page.type_query_user(usr)  # 输入用户手机号或姓名
        self.user_page.sel_query_role(role)  # 选择用户角色
        self.user_page.click_query_btn()  # 点击查询按钮
        time.sleep(2)
        screen_shot(self.driver, "用户查询.png")  # 截图
        if self.user_page.get_query_result_list_num():
            data_dic = self.user_page.get_data_dic_of_first()
            if usr == data_dic["姓名"]:
                self.assertEqual(usr, data_dic["姓名"])
            elif usr == data_dic["电话"]:
                self.assertEqual(usr, data_dic["电话"])
            else:
                self.fail("查询结果错误！")
        else:
            self.fail("没有查询到该用户，请检查测试数据！")

    @parameterized.expand(input=read_excel('user', 'reset_pwd'))
    def test_reset_pwd(self, operator_phone, operator_name, usr, expect1, expect2):
        """
         用户密码重置功能测试用例 。
        :param operator_phone: 操作者手机号
        :param operator_name: 操作者名称
        :param usr: 用户手机号或姓名
        :param expect1: 是否重置弹窗文案
        :param expect2: 确认重置文案
        :return: None
        """

        self.user_page.change_user(operator_phone, operator_name)   # 切换账号
        time.sleep(2)
        self.user_page.click_user_list_menu()    # 点击账号列表菜单
        time.sleep(2)
        self.user_page.query_by_name_or_phone(usr)   # 查询需要重置密码的用户
        time.sleep(2)
        result_num = self.user_page.get_query_result_list_num()
        if result_num and result_num == 1:  # 判断结果列表不为空且只有1条数据，则进行重置操作
            self.user_page.click_reset_btn()  # 点击重置按钮
            time.sleep(2)
            txt1 = self.user_page.get_reset_text()  # 获取是否确认重置文案
            screen_shot(self.driver, "重置密码1.png")  # 截图
            self.user_page.click_reset_ok()   # 点击确定按钮
            time.sleep(2)
            screen_shot(self.driver, "重置密码2.png")    # 截图
            txt2 = self.user_page.get_reset_ok_text()   # 获取重置成功文案
            self.assertEqual(expect1, txt1)     # 断言弹窗文案等于预期值
            self.assertEqual(expect2, txt2)     # 断言弹窗文案等于预期值
        else:
            screen_shot(self.driver, "重置密码-用户列表.png")
            self.fail("没有查询到该用户，请检查测试数据！")

    @parameterized.expand(input=read_excel('user', 'disable_user'))
    def test_disable_or_enable_user(self, operator_phone, operator_name, usr, expect1, expect2):
        """
         用户禁用和启用功能测试用例 。
        :param operator_phone: 操作者手机号
        :param operator_name: 操作者名称
        :param usr: 用户手机号或姓名
        :param expect1: 禁用成功预期值
        :param expect2: 启用成功预期值
        :return: None
        """

        self.user_page.change_user(operator_phone, operator_name)  # 切换到操作者账号
        time.sleep(2)
        self.user_page.click_user_list_menu()   # 点击账号列表菜单
        time.sleep(2)
        self.user_page.query_by_name_or_phone(usr)  # 查询出指定用户
        time.sleep(2)
        result_num = self.user_page.get_query_result_list_num()
        if result_num and result_num == 1:  # 判断结果列表不为空且只有1条数据，则进行禁用或启用操作
            if expect1:
                # 如果禁用按钮可见，则进行禁用操作，否则断言失败用户已处于禁用状态，
                if self.user_page.is_disable_btn_visible():
                    self.user_page.click_disable_btn()
                    time.sleep(2)
                    self.assertEqual(expect1, self.user_page.get_disable_ok_text())
                    self.assertFalse(self.user_page.is_disable_btn_visible())
                    screen_shot(self.driver, "禁用成功.png")
                else:
                    self.fail("该用户已被禁用，请检查测试数据！")

            elif expect2:
                # 如果禁用按钮可见，则断言失败用户已处于启用状态，否则进行启用操作
                if self.user_page.is_disable_btn_visible():
                    self.fail("该用户已被启用，请检查测试数据！")
                else:
                    self.user_page.click_enable_btn()
                    self.assertEqual(expect2, self.user_page.get_enable_ok_text())
                    self.assertTrue(self.user_page.is_disable_btn_visible())
                    screen_shot(self.driver, "启用成功.png")
            else:
                self.fail('没有预期值，无法进行断言，请检查测试数据！')
        else:
            screen_shot(self.driver, "禁用用户-用户列表.png")
            self.fail("没有查询到该用户，请检查测试数据！")

    @parameterized.expand(input=read_excel('user', 'look_user'))
    def test_look_user(self, operator_phone, operator_name, usr):
        """
         查看用户功能测试用例 。
        :param operator_phone:操作者手机号
        :param operator_name: 操作者名称
        :param usr: 用户手机号或姓名
        :return: None
        """

        self.user_page.change_user(operator_phone, operator_name)  # 切换到操作者账号
        time.sleep(2)
        self.user_page.click_user_list_menu()  # 点击用户列表菜单
        time.sleep(2)
        self.user_page.query_by_name_or_phone(usr)  # 查询出指定用户
        time.sleep(2)
        screen_shot(self.driver, "查看用户-用户列表.png")
        result_num = self.user_page.get_query_result_list_num()
        if result_num and result_num == 1:  # 判断结果列表不为空且只有1条数据，则进行查看用户操作
            self.user_page.click_look_btn()  # 点击查看按钮
            time.sleep(3)
            self.user_page.switch_window()  # 切换窗口
            screen_shot(self.driver, "查看用户-用户详情.png")
            self.assertEqual(usr, self.user_page.get_phone_value())  # 断言用户手机号正确
        else:
            self.fail("用户列表为空或数据不唯一，请检查测试数据！")


if __name__ == '__main__':
    unittest.main()
    # suite()

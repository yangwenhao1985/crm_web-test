import time
import unittest
from parameterized import parameterized
from test_case.models import MyUnit
from test_case.models.function import read_excel
from test_case.models.function import screen_shot
from test_case.page_obj.user_manage_page import UserManagePage
from test_case.page_obj.regist_manage_page import RegistManagePage

"""
@FileName: 学员管理测试类
@Author:吕永振
@Create on: 2017-06-14
@Update on: 2017-09-19
@Update by: Sixmiaomiao
"""


class RegistManageTestCase(MyUnit.MyTestOne):
    """ 报名管理测试类 """

    @parameterized.expand(input=read_excel('regist', 'query_regist'))
    def test_a_query_regist(self, operator_phone, operator_name, start_date, end_date, expect_value):
        """
        查询报名测试用例 。
        :param operator_phone: 操作者手机号
        :param operator_name: 操作者姓名
        :param start_date: 开始时间
        :param end_date: 结束时间
        :param expect_value: 预期值
        :return:
        """
        self.user_page.change_user(operator_phone, operator_name)  # 切换到操作者账号
        time.sleep(2)
        self.operation_page.click_regist_page()   # 点击报名信息列表
        time.sleep(2)
        self.operation_page.type_query_begin_date(start_date)        # 输入起始日期
        time.sleep(2)
        self.operation_page.type_query_end_date(end_date)            # 输入截止日期
        time.sleep(2)
        self.operation_page.click_query_btn()    # 点击查询按钮
        time.sleep(3)
        # 断言

        result_num = self.operation_page.get_query_result_list_num()
        if result_num and result_num == 1:
            screen_shot(self.driver, '查询报名管理.png')
            actual_value = self.operation_page.get_add_regist_message()
            self.assertEqual(expect_value, actual_value, msg="实际结果与预期结果不一致，请查看！")
        else:
            self.fail("查询结果列表为空或者数据不唯一，请检查测试数据！")

    @parameterized.expand(input=read_excel('regist', 'turn_page'))
    def test_b_jump_page(self, operator_phone, operator_name, jump_page, expect_value):
        """
        翻页跳转功能测试用例。
        :param operator_phone: 操作者手机号
        :param operator_name: 操作者姓名
        :param jump_page: 跳转页
        :param expect_value: 预期值
        :return:
        """
        self.user_page.change_user(operator_phone, operator_name)  # 切换到操作者账号
        time.sleep(2)
        self.operation_page.click_regist_page()     # 点击报名信息列表
        time.sleep(3)
        self.operation_page.click_last_page()       # 点击最后一页
        time.sleep(2)
        self.operation_page.click_previous_page()  # 点击上一页
        time.sleep(2)
        self.operation_page.click_next_page()       # 点击下一页
        time.sleep(2)
        self.operation_page.input_jump_page(jump_page)  # 输入需要跳转的页码
        time.sleep(2)
        self.operation_page.click_jump_btn()    # 点击跳转按钮
        time.sleep(2)
        # 断言
        actual_value = self.operation_page.get_current_page()
        self.assertEqual(expect_value, actual_value, msg="实际结果与预期结果不一致，请查看！")
        screen_shot(self.driver, '翻页跳转.png')


if __name__ == '__main__':
    unittest.main()


import time
import unittest
from parameterized import parameterized
from test_case.models.MyUnit import MyTestOne
from test_case.models.function import read_excel
from test_case.models.function import screen_shot

"""
@FileName: 学员管理测试类
@Author:Sixmiaomiao
@Create on: 2017-06-14
@Update on: 2017-09-19
@Update by: Sixmiaomiao
"""


class CallManageTestCase(MyTestOne):
    """ 通话记录管理测试类 """

    @parameterized.expand(input=read_excel('call', 'query_call'))
    def test_query_call(self,
                        operator_phone, operator_name, user_name, custom_name,
                        user_phone, custom_phone, begin_date,
                        end_date, status, expect_num):
        """
        通话记录查询测试用例。

        通过Excel文件获取测试数据，带入测试用例进行测试。

        :param operator_phone: 登录用户手机号
        :param operator_name: 登录用户姓名
        :param user_name: 查询条件-用户姓名
        :param custom_name: 查询条件-客户姓名
        :param user_phone: 查询条件-用户手机号
        :param custom_phone: 查询条件-客户手机号
        :param begin_date: 查询条件-开始日期
        :param end_date: 查询条件-结束日期
        :param status: 查询条件-通话状态
        :param expect_num: 预期查询条数
        :return: None
        """
        self.user_page.change_user(operator_phone, operator_name)  # 切换到操作者账号
        self.operation_page.click_call_list_menu()  # 点击通话记录菜单
        time.sleep(2)
        if user_name:
            self.operation_page.type_query_info(user_name)  # 输入用户姓名
        elif custom_name:
            self.operation_page.type_query_info(custom_name)  # 输入客户姓名
        elif user_phone:
            self.operation_page.type_query_info(user_phone)  # 输入用户手机
        elif custom_phone:
            self.operation_page.type_query_info(custom_phone)    # 输入客户手机
        else:
            self.operation_page.type_query_info("")      # 不输入
        self.operation_page.type_query_begin_date(begin_date)     # 输入起始日期
        self.operation_page.type_query_end_date(end_date)      # 输入结束日期
        self.operation_page.click_query_btn()  # 点击查询按钮
        time.sleep(2)
        if status:
            self.operation_page.sel_call_status(status)  # 选择通话记录状态
        time.sleep(2)
        real_num = self.operation_page.get_query_result_list_num()     # 获取查询结果列表条数
        if real_num:
            data_dic = self.operation_page.get_data_of_first()  # 获取查询结果第一行的数据
            if user_name:
                self.assertEqual(user_name, data_dic["姓名"], msg="姓名不正确！")
            elif custom_name:
                self.assertEqual(custom_name, data_dic["客户姓名"], msg="客户姓名不正确！")
            elif status:
                self.assertEqual(status, data_dic["status"], msg="通话状态不正确")
            else:
                self.fail("预期值全部为空，无法做断言！")
            self.assertEqual(expect_num, str(real_num), msg="查询结果条数不正确")
        else:
            self.fail("查询结果列表为空,请检查测试数据！")
        screen_shot(self.driver, "通话记录查询.png")

if __name__ == '__main__':
    unittest.main()
    # suite()

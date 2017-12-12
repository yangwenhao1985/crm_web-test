import time
import unittest
from parameterized import parameterized
from test_case.models.MyUnit import MyTestOne
from test_case.models.function import read_excel
from test_case.page_obj.daily_report_manage_page import DailyReportManagePage
from test_case.page_obj.user_manage_page import UserManagePage
from test_case.models.function import screen_shot

"""
@FileName: 学员管理测试类
@Author:Sixmiaomiao
@Create on: 2017-06-14
@Update on: 2017-09-20
@Update by: Sixmiaomiao
"""


class DailyReportManageTestCase(MyTestOne):
    """ 日报管理测试类 """

    @parameterized.expand(input=read_excel('daily_report', 'query_daily'))
    def test_query_daily_report(self, operator_phone, operator_name, company, user_name,
                                begin_date, end_date, phone, expect_num):
        """
         日报查询测试用例
        :param operator_phone: 操作者手机号
        :param operator_name: 操作者姓名
        :param company: 公司名称
        :param user_name: 用户名称
        :param begin_date: 开始日期
        :param end_date: 结束日期
        :param phone: 手机号
        :param expect_num: 预期值
        :return: None
        """

        self.user_page.change_user(operator_phone, operator_name)  # 切换到操作者账号
        time.sleep(2)
        self.operation_page.click_daily_report_list_menu()  # 点击日报管理页面菜单
        time.sleep(1)
        if company:
            self.operation_page.sel_query_company(company)  # 选择分公司
        else:
            pass
        self.operation_page.type_query_user_name(user_name)      # 输入员工姓名
        self.operation_page.type_query_begin_date(begin_date)     # 输入起始日期
        self.operation_page.type_query_end_date(end_date)      # 输入结束日期
        self.operation_page.click_query_btn()  # 点击查询按钮
        time.sleep(2)
        real_num = self.operation_page.get_query_result_list_num()
        screen_shot(self.driver, "日报查询.png")
        if real_num:
            self.assertEqual(real_num, int(expect_num))
            data_dic = self.operation_page.get_data_of_first()  # 获取查询结果第一行的数据
            self.assertEqual(user_name, data_dic['姓名'])
        else:
            self.fail("未查询到任何日报，请检查测试数据！")

    @parameterized.expand(input=read_excel('daily_report', 'look_daily'))
    def test_look_daily_report(self, operator_phone, operator_name, user_name, begin_date, end_date):
        """
         查看日报测试用例
        :param operator_phone: 操作者手机号
        :param operator_name: 操作者姓名
        :param user_name: 用户姓名
        :param begin_date: 开始日期
        :param end_date: 结束日期
        :return: None
        """

        self.user_page.change_user(operator_phone, operator_name)  # 切换到操作者账号
        time.sleep(2)
        self.operation_page.click_daily_report_list_menu()  # 点击日报管理页面菜单
        time.sleep(2)
        self.operation_page.query_by_username_date(user_name, begin_date, end_date)  # 查询出日报
        time.sleep(2)
        results = self.operation_page.get_query_result_list_num()  # 获取结果列表所有行
        screen_shot(self.driver, "查看-日报列表.png")
        if not results:
            self.fail("未查询到日报，请检查测试数据！")
        else:
            self.operation_page.click_look_btn()  # 点击查看按钮
            time.sleep(2)
            data_dic = self.operation_page.get_detail_data()  # 获取日报详情
            screen_shot(self.driver, "查看-日报详情.png")
            self.assertEqual(user_name, data_dic["user_name"], msg="员工姓名不正确！")
            self.assertTrue(begin_date in data_dic["report_time"], msg="上报时间不正确！")

if __name__ == '__main__':
    unittest.main()
    # suite()

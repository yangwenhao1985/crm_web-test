import unittest
import time
from parameterized import parameterized
from test_case.models import MyUnit
from test_case.models.function import read_excel
from test_case.models.function import screen_shot
from test_case.page_obj.user_manage_page import UserManagePage
from test_case.page_obj.venues_manage_page import VenuesManagePage

"""
@FileName: 学员管理测试类
@Author:吕永振
@Create on: 2017-06-14
@Update on: 2017-09-20
@Update by: Sixmiaomiao
"""


class VenuesManageTestCase(MyUnit.MyTestOne):
    """ 场馆管理测试类 """

    @parameterized.expand(input=read_excel('venues', 'query_venues'))
    def test_a_query_venues(self, operator_phone, operator_name, company_name, category, status, venues_name):
        """
        查询场馆测试用例。
        :param operator_phone: 操作者手机号
        :param operator_name: 操作者姓名
        :param company_name: 公司名称
        :param category: 科目
        :param status: 状态
        :param venues_name: 场馆名称
        :return:
        """
        self.user_page.change_user(operator_phone, operator_name)  # 切换到操作者账号
        time.sleep(2)
        self.operation_page.click_venues_list()  # 点击场馆列表
        time.sleep(2)
        if company_name:
            self.operation_page.sel_company(company_name)  # 选择分公司名称
        time.sleep(2)
        self.operation_page.click_query_btn()  # 点击查询按钮
        time.sleep(2)
        self.operation_page.sel_category(category)  # 选择科目
        time.sleep(2)
        self.operation_page.click_query_btn()  # 点击查询按钮
        time.sleep(2)
        self.operation_page.sel_venues_status(status)  # 选择场馆状态
        time.sleep(2)
        self.operation_page.click_query_btn()  # 点击查询按钮
        time.sleep(2)
        self.operation_page.input_venues(venues_name)  # 输入场馆名称
        time.sleep(2)
        self.operation_page.click_query_btn()  # 点击查询按钮
        time.sleep(2)
        screen_shot(self.driver, "查询场馆.png")
        result_num = self.operation_page.get_query_result_list_num()
        if result_num and result_num == 1:
            actual_value = self.operation_page.get_venues_message()
            self.assertEqual(venues_name, actual_value, msg="实际结果与预期结果不一致，请查看！")
        else:
            self.fail("查询结果列表为空或者数据不唯一，请检查测试数据！")

    @parameterized.expand(input=read_excel('venues', 'edit_venues'))
    def test_b_edit_venues(self, operator_phone, operator_name, query_category,
                           old_venues, new_venues_name, venues_address, longitude,
                           latitude, expect_value):
        """
        编辑场馆测试用例。
        :param operator_phone: 操作者手机号
        :param operator_name: 操作者姓名
        :param query_category: 查询科目
        :param old_venues: 原场馆名称
        :param new_venues_name: 新场馆名称
        :param venues_address: 场馆地址
        :param longitude: 经度
        :param latitude: 纬度
        :param expect_value: 预期值
        :return:
        """
        self.user_page.change_user(operator_phone, operator_name)  # 切换到操作者账号
        self.operation_page.click_venues_menu()  # 点击场馆管理菜单
        time.sleep(2)
        self.operation_page.click_venues_list()  # 点击场馆列表
        time.sleep(4)
        self.operation_page.sel_category(query_category)  # 选择科目
        time.sleep(2)
        self.operation_page.input_venues(old_venues)  # 输入场馆名称
        time.sleep(2)
        self.operation_page.click_query_btn()   # 点击查询按钮
        time.sleep(5)
        self.operation_page.click_venues_edit()  # 点击编辑场馆按钮
        time.sleep(2)
        self.operation_page.input_edit_name(new_venues_name)  # 输入场馆名称
        time.sleep(2)
        self.operation_page.input_edit_address(venues_address)  # 输入场馆地址
        time.sleep(2)
        self.operation_page.input_edit_longitude(str(longitude))  # 输入经度
        time.sleep(2)
        self.operation_page.input_edit_latitude(str(latitude))  # 输入纬度
        time.sleep(2)
        self.operation_page.click_edit_label()  # 勾选场馆类别
        time.sleep(2)
        self.operation_page.click_edit_btn()  # 点击确定按钮
        time.sleep(4)
        self.operation_page.click_venues_list()  # 点击场馆列表
        time.sleep(2)
        self.operation_page.sel_category(query_category)  # 选择科目
        time.sleep(2)
        self.operation_page.input_venues(new_venues_name)    # 输入场馆名称
        time.sleep(2)
        self.operation_page.click_query_btn()   # 点击查询按钮
        time.sleep(2)
        screen_shot(self.driver, "编辑场馆.png")
        result_num = self.operation_page.get_query_result_list_num()
        if result_num and result_num == 1:
            actual_value = self.operation_page.get_edit_venues_name()
            self.assertEqual(expect_value, actual_value, msg="实际结果与预期结果不一致，请查看！！！")
        else:
            self.fail("查询结果列表为空或者数据不唯一，请检查测试数据！")

    @parameterized.expand(input=read_excel('venues', 'add_venues'))
    def test_c_venues_add(self, operator_phone, operator_name, venues_name, venues_address,
                          longitude, latitude, status, expect_value):
        """
        添加场馆测试用例。
        :param operator_phone: 操作者手机号
        :param operator_name: 操作者姓名
        :param venues_name: 场馆名称
        :param venues_address: 场馆地址
        :param longitude: 经度
        :param latitude: 纬度
        :param status: 状态
        :param expect_value: 预期值
        :return:
        """
        self.user_page.change_user(operator_phone, operator_name)  # 切换到操作者账号
        time.sleep(3)
        self.operation_page.click_venues_add()  # 点击添加场馆菜单
        time.sleep(3)
        self.operation_page.input_venues_name(venues_name)   # 输入场馆名称
        time.sleep(3)
        self.operation_page.input_venues_address(venues_address)  # 输入场馆地址
        time.sleep(3)
        self.operation_page.input_venues_longitude(str(longitude))  # 输入经度
        time.sleep(3)
        self.operation_page.input_venues_latitude(str(latitude))  # 输入纬度
        time.sleep(2)
        self.operation_page.sel_venues_category1()  # 选择场馆包含的科目 （篮球）
        time.sleep(2)
        self.operation_page.sel_venues_category2()  # 选择场馆包含的科目 （羽毛球）
        time.sleep(2)
        self.operation_page.sel_venues_category3()  # 选择场馆包含的科目 （足球）
        time.sleep(2)
        self.operation_page.sele_venues_status(status)  # 选择场馆状态
        time.sleep(2)
        self.operation_page.venues_sure_btn()  # 点击保存按钮
        time.sleep(2)
        screen_shot(self.driver, '添加场馆.png')

        # 断言
        actual_value = self.operation_page.get_add_venues_message()
        self.assertEqual(expect_value, actual_value, msg="实际结果与预期结果不一致，请查看！")

    @parameterized.expand(input=read_excel('venues', 'del_venues'))
    def test_d_del_venues(self, operator_phone, operator_name, category, venues_name, expect_value):
        """
        删除场馆测试用例 。
        :param operator_phone: 操作者手机号
        :param operator_name: 操作者姓名
        :param category: 科目
        :param venues_name: 场馆名称
        :param expect_value: 预期值
        :return:
        """
        self.user_page.change_user(operator_phone, operator_name)  # 切换到操作者账号
        time.sleep(2)
        self.operation_page.click_venues_list()  # 点击场馆列表菜单
        time.sleep(2)
        self.operation_page.sel_category(category)  # 选择科目
        time.sleep(2)
        self.operation_page.input_venues(venues_name)  # 输入场馆名称
        time.sleep(2)
        self.operation_page.click_query_btn()  # 点击查询按钮
        time.sleep(3)
        self.operation_page.click_del_venues()  # 点击删除场馆按钮
        time.sleep(2)
        self.operation_page.del_affirm_venues()  # 点击确认按钮
        time.sleep(2)
        screen_shot(self.driver, '删除场馆.png')
        result_num = self.operation_page.get_query_result_list_num()
        if result_num and result_num == 1:
            actual_value = self.operation_page.get_del_venues_message()
            self.assertEqual(expect_value, actual_value, msg="实际结果与预期结果不一致，请查看！！")
        else:
            self.fail("查询结果列表为空或者数据不唯一，请检查测试数据！")


if __name__ == '__main__':
    unittest.main()

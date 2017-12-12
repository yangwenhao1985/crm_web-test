import time
import unittest
from parameterized import parameterized
from test_case.models.MyUnit import MyTestOne
from test_case.models.function import read_excel
from test_case.page_obj.course_manage_page import CourseManagePage
from test_case.page_obj.user_manage_page import UserManagePage
from test_case.models.function import screen_shot

"""
@FileName: 学员管理测试类
@Author:Sixmiaomiao
@Create on: 2017-06-14
@Update on: 2017-09-20
@Update by: Sixmiaomiao
"""


class CourseManageTestCase(MyTestOne):
    """排课管理测试类 """
    #
    # @parameterized.expand(input=read_excel('course', 'add_course'))
    # def test_add_course(self, operator_phone, operator_name, month, category,
    #                     venue, class_name, coach, expect1, expect2):
    #     """
    #      添加排课测试用例 。
    #     :param operator_phone: 操作者手机号
    #     :param operator_name: 操作者姓名
    #     :param month: 添加月份
    #     :param category: 科目
    #     :param venue: 场馆
    #     :param class_name: 班级
    #     :param coach: 教练
    #     :param expect1: 预期值1
    #     :param expect2: 预期值2
    #     :return: None
    #     """
    #
    #     self.user_page.change_user(operator_phone, operator_name)  # 切换到操作者账号
    #     time.sleep(2)
    #     self.operation_page.click_add_course_menu()  # 点击添加排课菜单
    #     time.sleep(2)
    #     self.operation_page.sel_month(month)  # 选择排课月份
    #     time.sleep(2)
    #     self.operation_page.sel_category(category)  # 选择科目
    #     time.sleep(2)
    #     self.operation_page.sel_venue(venue)   # 选择场馆
    #     time.sleep(2)
    #     if self.operation_page.deselect_class():
    #         if not self.operation_page.sel_class(class_name):  # 选择班级
    #             self.fail("选择班级失败，请检查测试数据！")
    #         time.sleep(2)
    #         self.operation_page.click_sel_coach_btn()  # 点击选择教练按钮
    #         time.sleep(2)
    #         self.operation_page.sel_coach(coach)  # 选择教练
    #         time.sleep(2)
    #         save_result = self.operation_page.save_course()  # 保存排课
    #         screen_shot(self.driver, "排课.png")  # 截图
    #         time.sleep(2)
    #         class_num = self.operation_page.get_class_num(venue)  # 获取班级数量
    #         self.assertEqual(expect1, save_result)  # 断言保存后的提示文案
    #         self.assertEqual(expect2, class_num)  # 断言保存后，场馆名称后的班级数量
    #     else:
    #         self.fail("该场馆下没有未排课的班级，请检查测试数据！")
    #
    # @parameterized.expand(input=read_excel('course', 'copy_course'))
    # def test_copy_course(self, operator_phone, operator_name, will_month, old_month, expect_value):
    #     """
    #      复制排课测试用例
    #     :param operator_phone:
    #     :param operator_name:
    #     :param will_month:
    #     :param old_month:
    #     :param expect_value:
    #     :return:
    #     """
    #
    #     self.user_page.change_user(operator_phone, operator_name)  # 切换到操作者账号
    #     time.sleep(1)
    #     self.operation_page.click_add_course_menu()  # 点击添加排课菜单项
    #     time.sleep(1)
    #     self.operation_page.copy_course(will_month, old_month)      # 复制排课
    #     self.assertEqual(expect_value, self.operation_page.get_result_text())  # 断言
    #
    # @parameterized.expand(input=read_excel('course', 'turn_page'))
    # def test_page_turn(self, operator_phone, operator_name):
    #     """
    #      翻页测试用例
    #     :param operator_phone: 操作者手机号
    #     :param operator_name: 操作者姓名
    #     :return: None
    #     """
    #
    #     self.user_page.change_user(operator_phone, operator_name)  # 切换到操作者账号
    #     time.sleep(2)
    #     self.operation_page.click_course_list_menu()
    #     time.sleep(2)
    #     self.turn_page_test(self.operation_page)
    #
    # @parameterized.expand(input=read_excel('course', 'look_course'))
    # def test_look_course(self, operator_phone, operator_name, month, expect):
    #     """
    #      查看排课测试用例
    #     :param operator_phone: 操作者手机号
    #     :param operator_name: 操作者姓名
    #     :param month: 查看月份
    #     :param expect: 预期值
    #     :return: None
    #     """
    #
    #     self.user_page.change_user(operator_phone, operator_name)  # 切换到操作者账号
    #     time.sleep(2)
    #     self.operation_page.click_course_list_menu()   # 点击排课列表菜单
    #     time.sleep(2)
    #     self.operation_page.query_course(month, month)     # 根据日期查询出指定排课
    #     time.sleep(2)
    #     if self.operation_page.get_query_result_list_num():
    #         self.operation_page.click_look_btn()   # 点击查看按钮
    #         time.sleep(2)
    #         txt = self.operation_page.get_text_of_look()  # 获取查看窗口的标题文字
    #         self.assertEqual(expect, txt, msg="查看窗口未打开")
    #         screen_shot(self.driver, "查看排课.png")
    #     else:
    #         self.fail("未查询到排课，请检查测试数据！")
    #
    # @parameterized.expand(input=read_excel('course', 'query_course'))
    # def test_query_course(self, operator_phone, operator_name, begin_date, end_date, status):
    #     """
    #      查询排课测试用例
    #     :param operator_phone: 操作者手机号
    #     :param operator_name: 操作者姓名
    #     :param begin_date: 开始日期
    #     :param end_date: 结束日期
    #     :param status: 排课状态
    #     :return: None
    #     """
    #
    #     self.user_page.change_user(operator_phone, operator_name)  # 切换到操作者账号
    #     time.sleep(1)
    #     self.operation_page.click_course_list_menu()  # 点击排课列表菜单
    #     time.sleep(1)
    #     self.operation_page.type_query_begin_date(begin_date)  # 输入起始日期
    #     self.operation_page.type_query_end_date(end_date)  # 输入结束日期
    #     self.operation_page.click_query_btn()  # 点击查询按钮
    #     time.sleep(1)
    #     self.operation_page.sel_course_status(status)  # 选择排课状态
    #     screen_shot(self.driver, "查询排课.png")
    #     time.sleep(2)
    #     if self.operation_page.get_query_result_list_num():  # 如果排课列表不为空，则获取列表第一行数据进行断言
    #         result_dic = self.operation_page.get_result_dict_of_first()
    #         self.assertTrue(end_date in result_dic["排课时间"])
    #         self.assertEqual(status, result_dic["status"])
    #     else:
    #         self.fail("未查询到排课，请检查测试数据！")
    #
    # @parameterized.expand(input=read_excel('course', 'edit_course'))
    # def test_edit_course(self, operator_phone, operator_name, date, category, venue,
    #                      class_name, old_coach, new_coach, expect):
    #     """
    #      编辑排课测试用例
    #     :param operator_phone:  操作者手机号
    #     :param operator_name: 操作者姓名
    #     :param date: 日期
    #     :param category: 科目
    #     :param venue: 场馆
    #     :param class_name: 班级
    #     :param old_coach: 原教练
    #     :param new_coach: 新教练
    #     :param expect: 预期值
    #     :return: None
    #     """
    #
    #     self.user_page.change_user(operator_phone, operator_name)  # 切换到操作者账号
    #     time.sleep(2)
    #     self.operation_page.click_course_list_menu()  # 点击排课列表菜单
    #     time.sleep(2)
    #     self.operation_page.query_course(date, date)  # 查询指定排课
    #     time.sleep(2)
    #     screen_shot(self.driver, "编辑排课-排课列表1.png")
    #     result_num = self.operation_page.get_query_result_list_num()
    #     if result_num and result_num == 1:  # 如果排课列表不为空，且为1条数据则进行编辑操作
    #         self.operation_page.click_edit_btn()  # 点击编辑按钮
    #         time.sleep(2)
    #         self.operation_page.switch_window()  # 切换标签页
    #         time.sleep(2)
    #         self.assertEqual(date, self.operation_page.get_course_month())    # 断言排课月份是否正确
    #         self.operation_page.click_hide_class()  # 显示已选班级
    #         time.sleep(2)
    #         self.operation_page.sel_category(category)  # 选择科目
    #         time.sleep(2)
    #         self.operation_page.sel_venue(venue)  # 选择场馆
    #         time.sleep(2)
    #         if self.operation_page.deselect_class():
    #             self.operation_page.sel_class(class_name)  # 选择班级
    #         else:
    #             self.fail("该场馆下没有班级，无法选择，请检查测试数据！")
    #         time.sleep(2)
    #         self.assertEqual(old_coach, self.operation_page.get_coach_name())  # 断言已选教练是否正确
    #         self.operation_page.click_sel_coach_btn()  # 点击已选教练按钮
    #         self.operation_page.sel_coach(new_coach)   # 更换教练
    #         time.sleep(2)
    #         save_result = self.operation_page.save_course()  # 保存排课
    #         time.sleep(2)
    #         self.assertEqual(expect, save_result)   # 断言是否保存成功
    #         screen_shot(self.driver, "编辑排课.png")
    #         self.operation_page.sel_category(category)     # 选择科目
    #         time.sleep(2)
    #         self.operation_page.sel_venue(venue)     # 点击场馆
    #         time.sleep(2)
    #         self.operation_page.sel_class(class_name)     # 点击班级
    #         time.sleep(2)
    #         self.assertEqual(new_coach, self.operation_page.get_coach_name())  # 断言教练是否修改成功
    #     else:
    #         self.fail("排课列表为空或结果不唯一，请检查测试数据！")

    @parameterized.expand(input=read_excel('course', 'audit_course'))
    def test_audit_course(self, operator_phone, operator_name, date, status, user_phone_city, user_phone_pianqu,
                          user_phone_head, expect):
        """
         排课审批用例
        :param operator_phone: 操作者手机号
        :param operator_name: 操作者姓名
        :param date: 日期
        :param status: 排课状态
        :param user_phone_city: 城市经理手机号
        :param user_phone_pianqu: 片区经理手机号
        :param user_phone_head: 总裁手机号
        :param expect: 预期值
        :return: None
        """

        self.user_page.change_user(operator_phone, operator_name)  # 切换到操作者账号
        time.sleep(1)
        self.operation_page.click_course_list_menu()   # 点击排课列表菜单
        time.sleep(2)
        self.operation_page.query_course(date, date)     # 根据日期查询出指定排课
        time.sleep(2)
        self.operation_page.sel_course_status(status)  # 选择状态
        time.sleep(2)
        result_num = self.operation_page.get_query_result_list_num()
        if result_num and result_num == 1:
            self.operation_page.click_submit_audit_btn()   # 点击提交审批
            time.sleep(2)
            self.operation_page.submit_audit_ok()  # 确认提交
            # 城市经理、片区经理、总裁三个人手机号的列表
            users = [user_phone_city, user_phone_pianqu, user_phone_head]
            for user in users:
                self.user_page.change_user(user)  # 切换到指定账号
                self.operation_page.click_course_menu()   # 点击排课管理菜单
                time.sleep(2)
                if user == user_phone_city or user == user_phone_pianqu:
                    self.operation_page.click_sub_company_audit()
                else:
                    self.operation_page.click_head_company_audit()     # 点击总公司审批菜单项
                self.operation_page.audit(operator_name, date, date)  # 审批排课
            time.sleep(2)
            self.user_page.change_user(operator_phone, operator_name)  # 切换账号
            time.sleep(2)
            self.operation_page.click_course_list_menu()   # 点击排课列表菜单
            time.sleep(2)
            self.operation_page.query_course(date, date)     # 根据日期查询出指定排课
            screen_shot(self.driver, "排课审核.png")
            time.sleep(2)
            dic = self.operation_page.get_result_dict_of_first()
            self.assertEqual(expect, dic["status"])
        else:
            self.fail("排课列表为空或者数量不唯一，请检查测试数据！")

if __name__ == '__main__':
    unittest.main()
    # suite()



import time
import unittest
from parameterized import parameterized
from test_case.models.MyUnit import MyTestOne
from test_case.models.function import read_excel
from test_case.page_obj.student_manage_page import StudentManagePage
from test_case.page_obj.user_manage_page import UserManagePage
from test_case.models.function import screen_shot

"""
@FileName: 学员管理测试类
@Author:Sixmiaomiao
@Create on: 2017-06-14
@Update on: 2017-09-19
@Update by: Sixmiaomiao
"""


class StudentManageTestCase(MyTestOne):
    """ 学员管理测试类 """

    @parameterized.expand(input=read_excel('student', 'query_student'))
    def test_query_student(
            self, operator_phone, operator_name, company, stname, teacher_name, begin_date, end_date,
            sex, birthday, parent, parent_phone, parent1, parent1_phone, teacher_phone):
        """ 学员查询测试用例 """

        self.user_page.change_user(operator_phone, operator_name)      # 切换账号
        time.sleep(2)
        self.operation_page.click_student_list_menu()  # 点击学员列表
        time.sleep(2)
        if company:
            self.operation_page.sel_query_company(company)     # 选择分公司
        else:
            pass
        self.operation_page.type_query_student(stname)      # 输入学员姓名或监护人手机号
        self.operation_page.type_query_teacher(teacher_name)      # 输入辅导老师姓名或辅导老师手机号
        self.operation_page.type_query_begin_date(begin_date)     # 输入起始日期
        self.operation_page.type_query_end_date(end_date)      # 输入结束日期
        self.operation_page.click_query_btn()  # 点击查询按钮
        time.sleep(2)
        data_dic = self.operation_page.get_data_of_first()
        self.assertEqual(stname, data_dic["姓名"], msg="学员姓名不正确！")
        self.assertEqual(company, data_dic["公司"], msg="所属公司不正确！")
        self.assertEqual(sex, data_dic["性别"], msg="学员性别不正确！")
        self.assertEqual(birthday, data_dic["生日"], msg="学员生日不正确！")
        self.assertEqual(parent, data_dic["监护人"], msg="监护人姓名不正确！")
        self.assertEqual(parent1, data_dic["备用监护人"], msg="备用监护人不正确！")
        self.assertEqual(parent_phone, data_dic["监护人手机号"], msg="监护人手机不正确！")
        self.assertEqual(parent1_phone, data_dic["备用监护人手机号"], msg="备用监护人手机不正确！")
        self.assertEqual(teacher_name, data_dic["辅导老师"], msg="辅导老师姓名不正确！")
        self.assertEqual(teacher_phone, data_dic["辅导老师手机号"], msg="辅导老师手机号不正确！")
        screen_shot(self.driver, "学员查询.png")

    @parameterized.expand(input=read_excel('student', 'look_student'))
    def test_look_student(
            self, operator_phone, operator_name, student_name, birthday, sex, parent
    ):
        """ 查看学员测试用例 """
        self.user_page.change_user(operator_phone, operator_name)      # 切换到操作者账号
        time.sleep(3)
        self.operation_page.click_student_list_menu()  # 点击学员列表
        time.sleep(2)
        self.operation_page.query_by_student_name_or_parent_phone(student_name)
        time.sleep(2)
        result_num = self.operation_page.get_query_result_list_num()
        if result_num and result_num == 1:
            self.operation_page.click_look_btn()
            time.sleep(2)
            data_dic = self.operation_page.get_detail_data_dic()
            self.assertEqual(student_name, data_dic["姓名:"], msg="学员姓名不正确！")
            self.assertEqual(sex, data_dic["性别:"], msg="学员性别不正确！")
            self.assertEqual(birthday, data_dic["生日:"], msg="学员生日不正确！")
            self.assertEqual(parent, data_dic["监护人姓名:"], msg="监护人姓名不正确！")
            screen_shot(self.driver, "查看用户-学员详情.png")
        else:
            screen_shot(self.driver, "查看用户-学员列表.png")
            self.fail("未查询到学员，请检查测试数据！")


if __name__ == '__main__':
    unittest.main()
    # suite()

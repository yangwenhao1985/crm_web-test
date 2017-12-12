import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from test_case.page_obj.base import Page
from selenium.webdriver.common.action_chains import ActionChains


class StudentManagePage(Page):
    # 菜单项
    student_menu_loc = (By.XPATH, "//a[text()=' 学员管理']")  # 菜单-学员管理
    student_list_loc = (By.XPATH, "//a[text()='学员列表']")  # 菜单-学员列表

    # 学员列表页面的元素
    query_stname_parentphone_loc = (By.ID, 'student-name')  # 查询条件--学生姓名或手机号
    query_teacher_name_phone_loc = (By.ID, 'tutoring-name')  # 查询条件--辅导老师姓名或手机号
    query_company_loc = (By.ID, 'company')  # 查询条件--请选择公司
    query_begin_date_loc = (By.ID, 'J-xl')  # 查询条件--起始日期
    query_end_date_loc = (By.ID, 'J-xl1')  # 查询条件--起始日期
    query_btn_loc = (By.ID, 'query')  # 查询按钮
    query_student_head_list = (By.XPATH, '//table[@class="student-table"]/thead/tr/th')  # 获取表头
    query_student_list = (By.XPATH, "//table[@class='student-table']/tbody/tr")  # 获取查询列表的行数
    query_student_list_first_loc = (By.XPATH, "//table[@class='student-table']/tbody/tr[1]/td")  # 获取第一行的所有td
    query_student_list_last_loc = \
        (By.XPATH, "//table[@class='student-table']/tbody/tr[last()]/td")  # 获取查询列表的最后一行的所有td
    query_last_page_loc = (By.XPATH, "//ul[@class='pagination']//input[@value='最后一页']")  # 最后一页元素

    # 查看学员详情页
    look_btn_loc = (By.CLASS_NAME, "look")  # 【查看】按钮

    student_info_labels_loc = (By.XPATH, "//form[@class='edit-form']/ul/li/span")  # 学员详情页所有Label
    student_info_values_loc = (By.XPATH, "//form[@class='edit-form']/ul/li/input[@type='text']")  # 学员详情页所有value
    detail_sex_man_loc = (By.ID, "man")  # 获取学员性别

    # 获取学员详情页的数据
    def get_detail_data_dic(self):
        return self.get_look_results_dic(self.student_info_labels_loc,
                                         self.student_info_values_loc,
                                         self.detail_sex_man_loc)

    # 获取查询结果列表中所有行
    def get_query_result_list_num(self):
        return self.get_list_num(*self.query_student_list)

    # 返回查询结果列表中最后一行的所有列的数据
    def get_data_of_last(self):
        return self.get_results_dic(self.query_student_head_list, *self.query_student_list_last_loc)

    # 返回查询结果列表中第一行的所有列的数据
    def get_data_of_first(self):
        return self.get_results_dic(self.query_student_head_list, self.query_student_list_first_loc)

    # 根据学员姓名或监护人手机号查询
    def query_by_student_name_or_parent_phone(self, student_name_or_parent_phone):
        self.type_query_student(student_name_or_parent_phone)
        self.click_query_btn()

    # 点击查看按钮
    def click_look_btn(self):
        target = self.find_element(*self.look_btn_loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
        time.sleep(1)
        target.click()

    # 点击学员管理菜单
    def click_student_menu(self):
        self.click(*self.student_menu_loc)

    # 点击学员列表菜单
    def click_student_list_menu(self):
        if self.is_student_list_visible():
            pass
        else:
            self.click_student_menu()
        self.click(*self.student_list_loc)

    # 点击查询按钮
    def click_query_btn(self):
        self.click(*self.query_btn_loc)

    # 输入查询条件--输入学生姓名或监护人手机号
    def type_query_student(self, stname_parentphone):
        self.type_text(stname_parentphone, *self.query_stname_parentphone_loc)

    # 输入查询条件--输入辅导老师姓名或辅导老师手机号
    def type_query_teacher(self, tech_name_or_phone):
        self.type_text(tech_name_or_phone, *self.query_teacher_name_phone_loc)

    # 输入查询条件--输入起始日期
    def type_query_begin_date(self, begin_date):
        # J-xl为控件id
        attribute_value = "document.getElementById('J-xl').readonly=false"
        date_value = "document.getElementById('J-xl').value=\"" + begin_date + "\""
        self.driver.execute_script(attribute_value)
        self.driver.execute_script(date_value)

    # 输入查询条件--输入结束日期
    def type_query_end_date(self, end_date):
        # J-xl1为控件id
        attribute_value = "document.getElementById('J-xl1').readonly=false"
        date_value = "document.getElementById('J-xl1').value=\"" + end_date + "\""
        self.driver.execute_script(attribute_value)
        self.driver.execute_script(date_value)

    # 输入查询条件--选择公司
    def sel_query_company(self, company_name):
        self.sel_value(company_name, *self.query_company_loc)

    # 判断学员列表菜单是否可见
    def is_student_list_visible(self):
        return self.is_element_visible(self.student_list_loc)


if __name__ == '__main__':
    pass

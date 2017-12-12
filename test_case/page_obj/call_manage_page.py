import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from test_case.page_obj.base import Page


class CallManagePage(Page):

    # 菜单项
    call_menu_loc = (By.XPATH, "//a[text()=' 通话记录管理']")  # 菜单-通话记录管理
    call_list_loc = (By.XPATH, "//a[text()='通话记录']")  # 菜单-通话记录

    # 通话记录列表页面的元素
    query_info_loc = (By.ID, 'call')  # 查询条件--可以输入员工姓名/客户姓名/员工手机号/客户手机号
    query_begin_date_loc = (By.ID, 'J-xl')  # 查询条件--起始日期
    query_end_date_loc = (By.ID, 'J-xl1')  # 查询条件--起始日期
    query_btn_loc = (By.ID, 'query')  # 查询按钮
    call_list_num = (By.XPATH, "//table[@class='call-table']/tbody/tr")     # 获取查询结果列表的行
    call_list_head_loc = (By.XPATH, "//table[@class='call-table']/thead/tr/th[position()=1 or position()>2]")   # 获取查询结果列表的表头
    call_list_first_loc = (By.XPATH, "//table[@class='call-table']/tbody/tr[1]/td")  # 获取第一行的所有td
    call_list_last_loc = \
        (By.XPATH, "//table[@class='call-table']/tbody/tr[last()]/td")     # 获取查询列表的最后一行的所有td
    query_last_page_btn_loc = (By.XPATH, "//ul[@class='pagination']//input[@value='最后一页']")     # 最后一页按钮元素
    call_status = (By.ID, "call-status")    # 通话状态

    # 获取查询结果列表中的行数
    def get_query_result_list_num(self):
        return self.get_list_num(*self.call_list_num)

    # 返回查询结果列表中最后一行的所有列的数据
    def get_data_of_last(self):
        return self.get_results_dic(self.call_list_head_loc, self.call_list_last_loc)

    # 返回查询结果列表中第一行的所有列的数据
    def get_data_of_first(self):
        return self.get_results_dic(self.call_list_head_loc, self.call_list_first_loc)

    # 根据员工姓名查询
    def query_by_username(self, user_name):
        self.type_query_info(user_name)

    # 根据客户姓名查询
    def query_by_custom_name(self, custom_name):
        self.type_query_info(custom_name)

    # 根据员工手机或客户手机查询
    def query_by_phone(self, phone):
        self.type_query_info(phone)

    # 选择通话状态
    def sel_call_status(self, status):
        self.sel_value(status, *self.call_status)

    # 点击通话记录管理菜单
    def click_call_menu(self):
        self.scroll_target(*self.call_menu_loc)  # 拖动到可见的元素去
        time.sleep(1)
        self.click(*self.call_menu_loc)

    # 点击通话记录列表菜单
    def click_call_list_menu(self):
        if not self.is_element_visible(self.call_list_loc):  # 判断通话记录列表菜单是否可见
            self.click_call_menu()  # 如果不可见，先点击通话记录管理菜单
        else:
            pass  # 否则略过
        self.scroll_target(*self.call_menu_loc)  # 拖动到可见的元素去
        time.sleep(1)
        self.click(*self.call_list_loc)  # 点击通话记录列表菜单

    # 点击查询按钮
    def click_query_btn(self):
        self.click(*self.query_btn_loc)

    # 输入查询条件-输入员工姓名或客户姓名或员工手机号或客户手机号
    def type_query_info(self, info):
        self.type_text(info, *self.query_info_loc)

    # 输入查询条件--输入起始日期
    def type_query_begin_date(self, begin_date):
        # J-xl为控件id
        self.type_value_by_id('J-xl', begin_date)

    # 输入查询条件--输入结束日期
    def type_query_end_date(self, end_date):
        # J-xl1为控件id
        self.type_value_by_id('J-xl1', end_date)

if __name__ == '__main__':
    pass

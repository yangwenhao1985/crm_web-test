import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from test_case.page_obj.base import Page


class DailyReportManagePage(Page):

    # 菜单项
    daily_report_menu_loc = (By.XPATH, "//a[text()=' 日报管理']")  # 菜单-日报管理
    daily_report_list_loc = (By.XPATH, "//a[text()='日报管理页面']")  # 菜单-日报管理页面

    # 日报列表页面的元素
    query_company_loc = (By.ID, 'company')  # 查询条件--请选择公司
    query_user_name_loc = (By.ID, 'employees-name')  # 查询条件--员工姓名
    query_begin_date_loc = (By.ID, 'J-xl')  # 查询条件--起始日期
    query_end_date_loc = (By.ID, 'J-xl1')  # 查询条件--起始日期
    query_btn_loc = (By.ID, 'query')  # 查询按钮
    daily_report_list_head_loc = (By.XPATH,'//table[@class="daily-table"]/thead/tr/th')     # 日报管理表头
    daily_report_list_num = (By.XPATH, "//table[@class='daily-table']/tbody/tr")     # 获取查询结果列表的行

    daily_report_list_first_loc = (By.XPATH, "//table[@class='daily-table']/tbody/tr[1]/td") # 获取第一行的所有td
    daily_report_list_last_loc = \
        (By.XPATH, "//table[@class='daily-table']/tbody/tr[last()]/td")     # 获取查询列表的最后一行的所有td
    query_last_page_btn_loc = (By.XPATH, "//ul[@class='pagination']//input[@value='最后一页']")     # 最后一页按钮元素

    # 日报详情页
    look_btn_loc = (By.XPATH, "//span[@class='look']")      # 【查看】按钮
    report_user_loc = (By.XPATH, "//span[text()='上报人：']/following-sibling::input")  # 获取上报人的值
    report_time_loc = (By.XPATH, "//span[text()='上报时间：']/following-sibling::input")  # 获取上报时间
    close_btn_loc = (By.ID, "shut")     # 获取日报详情页上的关闭按钮

    # 获取日报详情页的数据
    def get_detail_data(self):
        user_name = self.find_element(*self.report_user_loc).get_attribute("value")
        report_time = self.find_element(*self.report_time_loc).get_attribute("value")
        data_dic = {"user_name": user_name, "report_time": report_time}
        return data_dic

    # 获取查询结果列表的行数
    def get_query_result_list_num(self):
        return self.get_list_num(*self.daily_report_list_num)

    # 返回查询结果列表中最后一行的所有列的数据
    def get_data_of_last(self):
        return self.get_results_dic(self.daily_report_list_head_loc, *self.daily_report_list_last_loc)

    # 返回查询结果列表中第一行的所有列的数据
    def get_data_of_first(self):
        return self.get_results_dic(self.daily_report_list_head_loc, self.daily_report_list_first_loc)

    # 根据员工姓名和起止日期查询
    def query_by_username_date(self, user_name, begin_date, end_date):
        self.type_query_user_name(user_name)
        self.type_query_begin_date(begin_date)
        self.type_query_end_date(end_date)
        self.click_query_btn()

    # 点击查看按钮
    def click_look_btn(self):
        self.scroll_target(*self.look_btn_loc) # 拖动到可见的元素去
        time.sleep(1)
        self.click(*self.look_btn_loc)

    # 点击日报管理菜单
    def click_daily_report_menu(self):
        self.scroll_target(*self.daily_report_menu_loc)
        time.sleep(1)
        self.click(*self.daily_report_menu_loc)

    # 点击日报管理页面菜单
    def click_daily_report_list_menu(self):
        if self.is_daily_report_list_visible():
            pass
        else:
            self.click_daily_report_menu()
        self.click(*self.daily_report_list_loc)

    # 点击查询按钮
    def click_query_btn(self):
        self.click(*self.query_btn_loc)

    # 输入查询条件-输入员工姓名
    def type_query_user_name(self, user_name):
        self.type_text(user_name, *self.query_user_name_loc)

    # 输入查询条件--输入起始日期
    def type_query_begin_date(self, begin_date):
        # J-xl为控件id
        self.type_value_by_id('J-xl', begin_date)

    # 输入查询条件--输入结束日期
    def type_query_end_date(self, end_date):
        # J-xl1为控件id
        self.type_value_by_id('J-xl1', end_date)

    # 输入查询条件--选择公司
    def sel_query_company(self, company_name):
        self.sel_value(company_name, *self.query_company_loc)

    # 判断日报管理页面菜单是否可见
    def is_daily_report_list_visible(self):
        return self.is_element_visible(self.daily_report_list_loc)

if __name__ == '__main__':
    pass

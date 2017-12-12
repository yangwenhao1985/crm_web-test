import time
from selenium.webdriver.common.by import By
from test_case.page_obj.base import Page


class RegistManagePage(Page):

    # 查询报名信息
    regist_menu_loc = (By.XPATH, '//a[contains(text(),"报名信息管理")]')  # 报名信息管理
    regist_menu_page_loc = (By.XPATH, '//a[contains(text(),"报名信息列表")]')  # 报名信息列表
    query_btn_loc = (By.XPATH, "//input[@value='查询']")  # 查询按钮
    actual_value_loc = (By.XPATH, "//div[@id='page-wrapper']/table/tbody/tr/td[4]/a")  # 期望值
    regist_list_num = (By.XPATH, "//table[@class='sign-up-table']/tbody/tr")     # 获取查询结果列表的行

    # 翻页查询
    total_page_loc = (By.ID, 'total')  # 总页数
    first_page_loc = (By.XPATH, '//input[@value="第一页"]')  # 第一页按钮
    next_page_loc = (By.XPATH, '//input[@value="下一页"]')  # 下一页按钮
    previous_page_loc = (By.XPATH, '//input[@value="上一页"]')  # 上一页按钮
    last_page_loc = (By.XPATH, '//input[@value="最后一页"]')  # 最后一页
    jump_page_loc = (By.ID, 'jump_pages')  # 跳转输入框
    jump_button_loc = (By.ID, "jump")  # 跳转按钮

    # 点击报名信息管理
    def click_regist_menu(self):
        self.scroll_target(*self.regist_menu_loc) # 拖动到可见的元素去
        time.sleep(1)
        self.click(*self.regist_menu_loc)

    # 点击报名信息列表
    def click_regist_page(self):
        if self.is_regist_manage_page_visible():
            pass
        else:
            self.click_regist_menu()
        time.sleep(2)
        self.scroll_target(*self.regist_menu_page_loc)
        self.click(*self.regist_menu_page_loc)

    # 输入查询条件--输入起始日期
    def type_query_begin_date(self, begin_date):
        # J-xl为控件id
        self.type_value_by_id('J-xl', begin_date)

    # 输入查询条件--输入结束日期
    def type_query_end_date(self, end_date):
        # J-xl1为控件id
        self.type_value_by_id('J-xl1', end_date)

    # 点击查询按钮
    def click_query_btn(self):
        self.click(*self.query_btn_loc)

    # 判断报名信息列表 按钮是否可见
    def is_regist_manage_page_visible(self):
        return self.is_element_visible(self.regist_menu_page_loc)

    # 断言真实值
    def get_add_regist_message(self):
        return self.get_text(*self.actual_value_loc)

    # 翻页跳转功能
    # 点击第一页
    def click_first_page(self):
        self.click(*self.first_page_loc)

    # 点击上一页按钮
    def click_previous_page(self):
        self.click(*self.previous_page_loc)

    # 点击最后一页
    def click_last_page(self):
        self.click(*self.last_page_loc)

    # 点击下一页按钮
    def click_next_page(self):
        self.click(*self.next_page_loc)

    # 输入跳转的页码
    def input_jump_page(self, jump_page):
        self.type_text(jump_page, *self.jump_page_loc)

    # 点击跳转按钮
    def click_jump_btn(self):
        self.click(*self.jump_button_loc)

    # 断言 页面页数   该测试用例可用于获取总页数，及当前页
    def get_current_page(self):
        val_page = self.driver.find_element(*self.total_page_loc).get_attribute("value")
        list1 = val_page.split("/")
        cur_page = list1[0]
        return cur_page

    # 获取查询结果列表的行数
    def get_query_result_list_num(self):
        return self.get_list_num(*self.regist_list_num)


if __name__ == '__main__':
    pass

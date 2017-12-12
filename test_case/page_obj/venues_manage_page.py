import time
from config import get_config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from test_case.page_obj.base import Page


class VenuesManagePage(Page):
    """
    场馆管理Page对象类
    """

    # 查询场馆
    venues_menu_loc = (By.XPATH, '//a[contains(text(),"场馆管理")]')
    venues_list_loc = (By.XPATH, '//a[contains(text(),"场馆列表")]')
    venues_add_loc = (By.XPATH, '//a[contains(text(),"场馆添加")]')

    query_company_loc = (By.ID, 'company-id')        # 选择分公司
    query_category_loc = (By.ID, 'category-id')      # 选择科目
    input_venues_loc = (By.ID, 'venues-name')        # 输入场馆名称
    query_btn_loc = (By.XPATH, "//input[@value='查询']")           # 查询按钮
    venues_id = (By.XPATH, '//td[@class="venues-name"]')      # 获取搜索后的信息
    venues_status = (By.XPATH, "//select[@class='status']")          # 选择场馆状态
    query_venues_list = (By.XPATH, "//table[@class='venue-table']/tbody/tr")  # 获取查询列表的行数

    # 添加场馆
    input_venues_name_loc = (By.XPATH, '//input[@placeholder="输入场馆名称"]')      # 输入场馆名称
    input_venues_address_loc = (By.XPATH, '//input[@name = "address"]')    # 输入场馆地址
    input_venues_longitude_loc = (By.XPATH, '//input[@name = "longitude"]')      # 输入经度
    input_venues_latitude_loc = (By.XPATH, '//input[@name = "latitude"]')      # 输入纬度
    sel_venues_category1_loc = (By.XPATH, '//label[@for ="category1"]')        # 包含科目 选择 篮球
    sel_venues_category2_loc = (By.XPATH, '//label[@for ="category2"]')        # 包含科目 选择  羽毛球
    sel_venues_category3_loc = (By.XPATH, '//label[@for ="category3"]')        # 包含科目 选择 足球
    sel_venues_status_loc = (By.XPATH, '//select[@id="status"]')        # 选择场馆状态
    venues_sure_btn_loc = (By.XPATH, '//input[@class="venue-add-save"]')   # 确定按钮
    get_add_venues_loc = (By.XPATH, '//p[@class = "p2"]')     # 获取添加成功的提示文本

    # 编辑场馆
    venues_edit_loc = (By.XPATH, '//span[@class="edit"]')        # 编辑场馆按钮
    venues_edit_name = (By.ID, "name")       # 编辑场馆名称
    venues_edit_address = (By.ID, "address")     # 编辑场馆地址
    venues_edit_label = (By.XPATH, "//input[@id='category1']")           # 选择场馆类别为篮球
    venues_edit_btn = (By.XPATH, "//input[@value='确定']")                 # 确定按钮
    get_edit_venues_name_loc = (By.XPATH, '//td[@class="venues-name"]/a')         # 第一列场馆名称

    # 删除场馆
    del_venues_loc = (By.XPATH,'//span[@class="delete"]')       # 删除场馆按钮
    del_affirm_venues_loc =(By.XPATH, '//p[@class = "p3"]/input[@value = "确定"]')
    del_venues_message_loc = (By.XPATH, '//p[@class = "p2"]')

    # 点击删除按钮
    def click_del_venues(self):
        self.click(*self.del_venues_loc)

    # 点击删除场馆弹窗的确定按钮
    def del_affirm_venues(self):
        self.click(*self.del_affirm_venues_loc)

    # 验证弹窗出现后的文本显示内容
    def get_del_venues_message(self):
        return self.get_text(*self.del_venues_message_loc)

    # 点击场馆添加按钮
    def click_venues_add(self):
        if self.is_venues_add_visible():
            pass
        else:
            self.click_venues_menu()
        time.sleep(2)
        self.click(*self.venues_add_loc)

    # 输入场馆名称
    def input_venues_name(self, add_venues_name):
        self.type_text(add_venues_name, *self.input_venues_name_loc)

    # 输入场馆地址
    def input_venues_address(self, add_venues_address):
        self.type_text(add_venues_address, *self.input_venues_address_loc)

    # 输入经度
    def input_venues_longitude(self, venues_longitude):
        self.type_text(venues_longitude, *self.input_venues_longitude_loc)

    # 输入纬度
    def input_venues_latitude(self, venues_latitude):
        self.type_text(venues_latitude, *self.input_venues_latitude_loc)

    # 选择场馆包含的科目(篮球)
    def sel_venues_category1(self):
        self.click(*self.sel_venues_category1_loc)

    # 选择场馆包含的科目（羽毛球）
    def sel_venues_category2(self):
        self.click(*self.sel_venues_category2_loc)

    # 选择场馆包含的科目（足球）
    def sel_venues_category3(self):
        self.click(*self.sel_venues_category3_loc)

    # 选择场馆状态
    def sele_venues_status(self, sele_venues_status):
        self.sel_value(sele_venues_status, *self.sel_venues_status_loc)

    # 点击确定按钮
    def venues_sure_btn(self):
        self.click(*self.venues_sure_btn_loc)

    # 获取保存成功信息---添加场馆断言用
    def get_add_venues_message(self):
        return self.get_text(*self.get_add_venues_loc)

    # 判断添加场馆按钮是否可见
    def is_venues_add_visible(self):
        return self.is_element_visible(self.venues_add_loc)

    # 模块一  编辑场馆
    # 点击编辑按钮
    def click_venues_edit(self):
        self.click(*self.venues_edit_loc)

    # 输入编辑的场馆名称
    def input_edit_name(self, edit_name):
        self.type_text(edit_name, *self.venues_edit_name)

    # 输入场馆地址
    def input_edit_address(self, edit_address):
        self.type_text(edit_address, *self.venues_edit_address)

    # 输入经度
    def input_edit_longitude(self, venues_longitude):
        self.type_text(venues_longitude, *self.input_venues_longitude_loc)

    # 输入纬度
    def input_edit_latitude(self, venues_latitude):
        self.type_text(venues_latitude, *self.input_venues_latitude_loc)

    # 勾选场馆类别
    def click_edit_label(self):
        self.click(*self.venues_edit_label)

    # 点击确定按钮
    def click_edit_btn(self):
        self.click(*self.venues_edit_btn)

    # 获取场馆名称--编辑场馆断言用
    def get_edit_venues_name(self):
        return self.get_text(*self.get_edit_venues_name_loc)

    # 点击场馆管理菜单
    def click_venues_menu(self):
        self.click(*self.venues_menu_loc)

    # 点击添加场馆菜单
    def click_venues_list_add(self):
        if self.is_venues_list_visible():
            pass
        else:
            self.click_venues_menu()
        self.click(*self.venues_add_loc)

    # 点击场馆列表菜单
    def click_venues_list(self):
        if self.is_venues_list_visible():
            pass
        else:
            self.click_venues_menu()
        self.click(*self.venues_list_loc)

    #  选择分公司
    def sel_company(self, company):
        self.sel_value(company, *self.query_company_loc)

    #   选择科目
    def sel_category(self, category):
        self.sel_value(category, *self.query_category_loc)

    # 输入场馆名称
    def input_venues(self, venues_name):
        self.type_text(venues_name, *self.input_venues_loc)

    # 点击查询按钮
    def click_query_btn(self):
        self.click(*self.query_btn_loc)

    # 获取输入信息
    def get_venues_message(self):
        return self.get_text(*self.venues_id)

    # 选择场馆状态
    def sel_venues_status(self, status):
        self.sel_value(status, *self.venues_status)

    # 判断场馆列表是否可见
    def is_venues_list_visible(self):
        return self.is_element_visible(self.venues_list_loc)

    # 获取查询结果列表中所有行
    def get_query_result_list_num(self):
        return self.get_list_num(*self.query_venues_list)

if __name__ == '__main__':
    pass
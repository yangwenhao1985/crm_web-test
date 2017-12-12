import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from test_case.page_obj.base import Page
from test_case.page_obj.login_manage_page import LoginManagePage
import config


class UserManagePage(Page):

    # 菜单项
    user_menu_loc = (By.XPATH, "//a[contains(text(),'账号管理')]")  # 菜单-账号管理
    user_list_loc = (By.XPATH, "//a[contains(text(),'账号列表')]")  # 菜单-账号列表
    add_user_menu_loc = (By.XPATH, "//a[contains(text(),'添加账号')]")  # 菜单-添加账号
    change_back_user_menu_loc = (By.XPATH, "//a[text()='切回']")  # 切回

    # 添加账号页面的元素
    department_sel_loc = (By.ID, "department-list")  # 部门
    role_sel_loc = (By.ID, "role-id")  # 岗位
    superior_sel_loc = (By.ID, "superior")  # 上级
    userLevel_sel_loc = (By.ID, "user-level")  # 职级
    name_loc = (By.XPATH, "//input[@placeholder='请输入姓名']")  # 用户姓名
    phone_loc = (By.ID, 'phone')  # 手机号
    webchat_loc = (By.XPATH, "//input[@placeholder='请输入微信号']")  # 微信号
    woman_sex_loc = (By.ID, 'woman')  # 性别女
    man_sex_loc = (By.ID, 'man')    # 性别男
    email_loc = (By.ID, "email")  # 邮箱
    pic_loc = (By.XPATH, "//p[text()='点击上传头像']")  # 头像占位图
    upload_btn_loc = (By.ID, "upload")  # 上传图片按钮
    pop_text_loc = (By.XPATH, "//div[@class='pop']/p[@class='p2']")     # 保存后弹出的提示文案
    save_btn_loc = (By.XPATH, "//input[@class='save']")  # 保存按钮

    # 账号列表页面的元素
    query_user_loc = (By.ID, 'user-name')  # 查询条件--用户名或手机号
    query_role_loc = (By.ID, 'role')  # 查询条件--职位
    query_company_loc = (By.ID, 'company')  # 查询条件--公司
    query_btn_loc = (By.ID, 'query')  # 查询按钮
    user_list_num = (By.XPATH, "//table[@class='user-table']/tbody/tr")  # 获取查询结果列表的所有行
    user_list_head_loc = (By.XPATH, "//table[@class='user-table']/thead/tr/th")  # 获取查询结果列表的表头
    user_list_first_loc = (By.XPATH, "//table[@class='user-table']/tbody/tr[1]/td")  # 获取第一行的所有td

    switch_btn_loc = (By.CLASS_NAME, "switch")    # 【切换】按钮
    edit_btn_loc = (By.CLASS_NAME, "edit")  # 【编辑】按钮
    disable_btn_loc = (By.CLASS_NAME, "disable")    # 【禁用】按钮
    disable_ok_btn_loc = (By.XPATH, "//div[@id='disable']//input[@value='确定']")  # 确认禁用弹窗的【确定】按钮
    enable_btn_loc = (By.CLASS_NAME, "enable")  # 【启用】按钮
    enable_ok_btn_loc = (By.XPATH, "//div[@id='enable']//input[@value='确定']")  # 确认启用弹窗的【确定】按钮
    look_btn_loc = (By.CLASS_NAME, "look")      # 【查看】按钮

    reset_btn_loc = (By.CLASS_NAME, "reset")    # 【重置】按钮
    reset_text_loc = (By.XPATH, "//div[@id='reset']/p[@class='p2 text']")   # 重置弹窗文案
    reset_ok_loc = (By.XPATH, "//div[@id='reset']//input[@value='确定']")     # 重置弹窗的确定按钮
    ok_text_loc = (By.XPATH, "//div[@id='wrapper']/div[@class='pop']//p[@class='p2']")      # 确定弹窗的文案

    # 根据用户名或手机号查询用户
    def query_by_name_or_phone(self, name_or_phone):
        self.type_query_user(name_or_phone)
        time.sleep(2)
        self.click_query_btn()

    # 获取手机号字段的值
    def get_phone_value(self):
        return self.get_value(*self.phone_loc)

    # 点击【重置】按钮
    def click_reset_btn(self):
        self.click(*self.reset_btn_loc)

    # 获取确认重置弹窗文案
    def get_reset_text(self):
        return self.get_text(*self.reset_text_loc)

    # 点击【确定】按钮
    def click_reset_ok(self):
        self.click(*self.reset_ok_loc)

    # 获取重置成功弹窗文案
    def get_reset_ok_text(self):
        return self.get_text(*self.ok_text_loc)

    # 点击禁用按钮
    def click_disable_btn(self):
        self.click(*self.disable_btn_loc)

    # 确定禁用并获取文案
    def get_disable_ok_text(self):
        self.click(*self.disable_ok_btn_loc)
        time.sleep(2)
        return self.get_text(*self.ok_text_loc)

    # 点击启用按钮
    def click_enable_btn(self):
        self.click(*self.enable_btn_loc)

    # 确定启用并获取文案
    def get_enable_ok_text(self):
        self.click(*self.enable_ok_btn_loc)
        time.sleep(2)
        return self.get_text(*self.ok_text_loc)

    # 点击查看按钮
    def click_look_btn(self):
        self.click(*self.look_btn_loc)

    # 点击编辑按钮
    def click_edit_btn(self):
        self.click(*self.edit_btn_loc)

    # 点击账号管理菜单
    def click_user_menu(self):
        self.click(*self.user_menu_loc)

    # 点击添加账号菜单
    def click_add_user_menu(self):
        if self.is_user_list_visible():
            pass
        else:
            self.click_user_menu()
        time.sleep(2)
        self.click(*self.add_user_menu_loc)

    # 点击账号列表菜单
    def click_user_list_menu(self):
        if self.is_user_list_visible():
            pass
        else:
            self.click_user_menu()
        time.sleep(2)
        self.click(*self.user_list_loc)

    # 点击切换按钮（测试固定选择定西分公司的运营经理进行切换）
    def click_switch_btn(self):
        self.click(*self.switch_btn_loc)

    # 点击查询按钮
    def click_query_btn(self):
        self.click(*self.query_btn_loc)

    # 输入查询条件--输入用户名或手机号
    def type_query_user(self, user_name):
        self.type_text(user_name, *self.query_user_loc)

    # 输入查询条件--选择岗位
    def sel_query_role(self, role_name):
        self.sel_value(role_name, *self.query_role_loc)

    # 输入查询条件--选择公司
    def sel_query_company(self, company_name):
        self.sel_value(company_name, *self.query_company_loc)

    # 输入账号姓名
    def type_user_name(self, name):
        self.type_text(name, *self.name_loc)

    # 输入账号手机号
    def type_user_phone(self, phone):
        self.type_text(phone, *self.phone_loc)

    # 输入微信号
    def type_webchat(self, webchat):
        self.type_text(webchat, *self.webchat_loc)

    # 选择性别
    def sel_sex(self, sex):
        if sex == '男':
            self.click(*self.man_sex_loc)
        else:
            self.click(*self.woman_sex_loc)

    # 选择部门
    def sel_dept(self, dept):
        self.sel_value(dept, *self.department_sel_loc)

    # 选择岗位
    def sel_role(self, role):
        self.sel_value(role, *self.role_sel_loc)

    # 选择上级
    def sel_superior(self, superior):
        self.sel_value(superior, *self.superior_sel_loc)

    # 选择职级
    def sel_user_level(self, level):
        self.sel_value(level, *self.userLevel_sel_loc)

    # 输入邮箱
    def type_email(self, email):
        self.type_text(email, *self.email_loc)

    # 上传头像
    def upload_pic(self, pic):
        self.find_element(*self.pic_loc).click()  # 定位头像占位图点击
        time.sleep(3)
        os.system(config.get_config('directory', 'upload_pic1'))
        time.sleep(5)
        os.system(config.get_config('directory', 'upload_pic2') + ' ' + pic)
        time.sleep(5)
        self.find_element(*self.upload_btn_loc).click()

    # 点击保存按钮
    def click_save_btn(self):
        self.click(*self.save_btn_loc)

    # 获取弹窗信息
    def get_pop_text(self):
        return self.get_text(*self.pop_text_loc)

    def get_data_dic_of_first(self):
        return self.get_results_dic(self.user_list_head_loc, self.user_list_first_loc)

    # 判断账号列表菜单是否可见
    def is_user_list_visible(self):
        return self.is_element_visible(self.user_list_loc)

    # 判断禁用按钮是否可见
    def is_disable_btn_visible(self):
        return self.is_element_visible(self.disable_btn_loc)

    # 获取查询结果列表中的行数
    def get_query_result_list_num(self):
        return self.get_list_num(*self.user_list_num)

    # 切换账号
    def _change_user(self, user_phone):
        if self.is_user_list_visible():
            pass
        else:
            self.click_user_menu()
        time.sleep(2)
        self.click_user_list_menu()
        time.sleep(2)
        self.query_by_name_or_phone(user_phone)
        time.sleep(2)
        self.click_switch_btn()  # 切换到指定的用户
        time.sleep(2)

    # 切换账号(先判断当前登录用户是否为要切换的用户，如果不是再判断是否为用于切换账号的用户[李磊或赵曰鹏]，是则切换账号;否则先切回再切换)
    def change_user(self, switch_to_user_phone, switch_to_user_name=""):

        # 创建登录页的Page对象
        login_page = LoginManagePage(self.driver, self.url)
        time.sleep(2)
        # 获取当前登录用户的姓名
        current_login_user_name = login_page.get_hello_text().split(':')[1].strip()
        # 从配置文件获取用于切换账号的用户用户名称
        init_user_name = config.get_config("login", "username")

        if current_login_user_name != switch_to_user_name:  # 如果当前登录用户不是想要切换的用户
            if current_login_user_name != init_user_name:  # 如果当前登录用户不是可切换账号的用户
                self.change_back_user()  # 点击切回，切回到可切换账号的用户
            else:
                pass
            time.sleep(2)
            self._change_user(switch_to_user_phone)  # 切换用户
            time.sleep(2)
        else:
            time.sleep(1)
            pass

    # 切回
    def change_back_user(self):
        self.click(*self.change_back_user_menu_loc)

if __name__ == '__main__':
    pass

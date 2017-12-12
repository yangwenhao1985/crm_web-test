import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from test_case.page_obj.base import Page


class CourseManagePage(Page):
    # 菜单项
    course_menu_loc = (By.XPATH, "//a[text()=' 排课管理']")  # 菜单-排课管理菜单
    course_list_loc = (By.XPATH, "//a[text()='排课列表']")  # 菜单-排课列表
    course_add_loc = (By.XPATH, "//a[text()='添加排课']")  # 菜单-添加排课

    # 排课列表页面的元素
    query_company_loc = (By.ID, "company")  # 查询条件--公司
    query_begin_date_loc = (By.ID, 'J-xl')  # 查询条件--起始日期
    query_end_date_loc = (By.ID, 'J-xl1')  # 查询条件--起始日期
    query_btn_loc = (By.ID, 'query')  # 查询按钮
    look_btn_loc = (By.CLASS_NAME, 'look')      # 查看按钮
    look_title_loc = (By.XPATH, "//div[@id='table-box']/h3")  # 查看窗口的标题
    course_list = (By.XPATH, "//table[@class='time-table']/tbody/tr")  # 获取查询结果列表的所有行
    course_list_table_head = (By.XPATH, "//table[@class='time-table']/thead/tr/th")     # 获取查询结果列表的表头
    course_list_first_loc = (By.XPATH, "//table[@class='time-table']/tbody/tr[1]/td")  # 获取第一行的所有td
    course_list_last_loc = \
        (By.XPATH, "//table[@class='time-table']/tbody/tr[last()]/td")  # 获取查询列表的最后一行的所有td
    query_last_page_btn_loc = (By.XPATH, "//ul[@class='pagination']//input[@value='最后一页']")  # 最后一页按钮元素
    course_status = (By.ID, "sub-company-status")  # 获取审批状态
    edit_btn_loc = (By.CLASS_NAME, "edit")      # 编辑按钮
    submit_audit_btn_loc = (By.CLASS_NAME, "submit-audit")  # 提交审批按钮
    submit_audit_ok_btn_loc = (By.XPATH, "//div[@id='examine']//input[@value='确定']")    # 确认提交审批弹窗中的确定按钮
    sub_company_audit_menu_loc = (By.XPATH, "//ul[@id='side-menu']//a[text()='分公司审批']")     # 分公司审批菜单项
    audit_btn_loc = (By.XPATH, ".//div[@id='page-wrapper']//span[@class='examine']")    # 审核按钮
    audit_ok_btn_loc = (By.XPATH, "//div[@id='table']/input[@class='determine']")   # 审核同意按钮
    audit_no_btn_loc = (By.XPATH, "//div[@id='table']/input[@class='shut1']")   # 审核不同意按钮
    company_audit_menu_loc = (By.XPATH, "//ul[@id='side-menu']//a[text()='总公司审批']")


    # 添加排课页面的元素定位
    month_loc = (By.ID, "month")  # 请选择月份
    copy_btn_loc = (By.XPATH, "//input[@class='copy']")  # 复制按钮
    copy_month_loc = (By.ID, "month2")  # 要复制几月份的课
    copy_ok_loc = (By.CLASS_NAME, "determine")      # 复制弹窗---确定
    copy_cancle_loc = (By.CLASS_NAME, "shut1")      # 复制弹窗---取消

    hide_btn_loc = (By.ID, "is-hide-selected-class")  # 隐藏已选课班级
    category_loc = (By.ID, "category")  # 请选择科目
    venue_names_loc = (By.XPATH, "//span[@class='venue-name']")  # 场馆元素（一组元素）
    deselect_class_loc = (By.XPATH, "//article[@id='right']//span")  # 待选班级元素（一组）
    select_class_loc = (By.XPATH, "//article[@id='center']//span")  # 已选班级元素（一组）
    coach_btn_loc = (By.XPATH, "//article[@id='coach']//input[@class='coach-button']")  # 请选择教练按钮
    search_coach_name_loc = (By.ID, "coach-name")  # 输入教练姓名
    search_btn_loc = (By.ID, "seach")  # 搜索按钮
    sel_coach_loc = (By.XPATH, "//input[@name='coach']/following-sibling::label")  # 教练
    sel_save_btn_loc = (By.ID, "coach-save")  # 保存按钮
    sel_coach_name_loc = (By.XPATH, "//article[@id='coach']/div/ul/li")  # 已选教练名称
    save_btn_loc = (By.XPATH, "//section[@class='time-table-add']//input[@value='保存']")  # 保存排课按钮
    result_text_loc = (By.XPATH, "//div[@id='wrapper']/div[@class='pop']//p[@class='p2']")  # 保存结果弹窗文案
    page_loc = (By.ID, "total")

    # 获取查询结果列表中的行数
    def get_query_result_list_num(self):
        return self.get_list_num(*self.course_list)

    # 返回查询结果列表中第一行的所有列的数据
    # 例如:['编号'：149，'排课人'：'test']
    def get_result_dict_of_first(self):
        return self.get_results_dic(self.course_list_table_head, self.course_list_first_loc)

    # 选择排课状态
    def sel_course_status(self, status):
        self.sel_value(status, *self.course_status)

    # 点击排课管理菜单
    def click_course_menu(self):
        self.click(*self.course_menu_loc)

    # 点击排课列表菜单
    def click_course_list_menu(self):
        if not self.is_element_visible(self.course_list_loc):
            self.click_course_menu()
        else:
            pass
        self.click(*self.course_list_loc)

    # 点击提交审批按钮
    def click_submit_audit_btn(self):
        self.click(*self.submit_audit_btn_loc)

    # 确认提交审批
    def submit_audit_ok(self):
        self.click(*self.submit_audit_ok_btn_loc)

    # 点击审核按钮
    def click_audit_btn(self):
        self.click(*self.audit_btn_loc)

    # 同意
    def audit_ok(self):
        self.click(*self.audit_ok_btn_loc)

    # 不同意
    def audit_no(self):
        self.click(*self.audit_no_btn_loc)

    # 点击分公司审批菜单项
    def click_sub_company_audit(self):
        if not self.is_element_visible(self.sub_company_audit_menu_loc):
            self.click_course_menu()
        else:
            pass
        self.click(*self.sub_company_audit_menu_loc)

    # 点击总公司审批菜单项
    def click_head_company_audit(self):
        if not self.is_element_visible(self.company_audit_menu_loc):
            self.click_course_menu()
        else:
            pass
        self.click(*self.company_audit_menu_loc)

    # 审批
    def audit(self, paike_user, begin_date, end_date, company_name=""):
        self.query_course(begin_date, end_date, company_name)
        time.sleep(1)
        course_list = self.get_result_dict_of_first()
        if course_list:
            if paike_user == course_list["排课人"]:
                time.sleep(2)
                self.click_audit_btn()
                time.sleep(2)
                self.audit_ok()
            else:
                print("排课人错误")
        else:
            print("course_manage_page:列表为空，没有待审核的排课")

    # 点击查询按钮
    def click_query_btn(self):
        self.click(*self.query_btn_loc)

    # 输入查询条件--选择公司
    def sel_company(self, company_name):
        self.sel_value(company_name, *self.query_company_loc)

    # 输入查询条件--输入起始日期
    def type_query_begin_date(self, begin_time):
        # begin-time是控件的class_name
        self.type_value_by_class_name('begin-time', begin_time)

    # 输入查询条件--输入结束日期
    def type_query_end_date(self, end_time):
        # end-time是控件的class_name
        self.type_value_by_class_name('end-time', end_time)

    # 点击添加排课菜单项
    def click_add_course_menu(self):
        if self.is_element_visible(self.course_list_loc):
            pass
        else:
            self.click_course_menu()
        time.sleep(2)
        self.click(*self.course_add_loc)

    # 选择要排课的月份
    def sel_month(self, date):
        self.type_value_by_id('month', date)

    # 选择科目
    def sel_category(self, category):
        self.sel_value(category, *self.category_loc)

    # 返回场馆名称后的班级数量
    def get_class_num(self, venue):
        venues = self.find_elements(*self.venue_names_loc)
        if venues:
            for v in venues:
                if v.text == venue:
                    return self.find_element(By.XPATH,
                                             "//span[@class='venue-name']"
                                             "[text()='" + venue + "']/../following-sibling::span").text
                else:
                    return ""
        else:
            print("场馆列表为空")
            return ""

    # 点选场馆
    def sel_venue(self, venue):
        venues = self.find_elements(*self.venue_names_loc)
        if venues:
            for v in venues:
                if v.text == venue:
                    v.click()
                    break
            else:
                print("要选择的场馆不存在，请检查测试数据")
        else:
            print("场馆列表为空")

    # 获取所有待选班级
    def deselect_class(self):
        return self.find_elements(*self.deselect_class_loc)

    # 点选班级
    def sel_class(self, class_name):
        classes = self.deselect_class()
        for c in classes:
            if c.text == class_name:
                c.click()
                break
            else:
                continue
        else:
            return False
        return True

    # 获取已选班级的名字
    def get_sel_class_name(self):
        return self.get_text(*self.select_class_loc)

    # 点击选择教练按钮
    def click_sel_coach_btn(self):
        self.click(*self.coach_btn_loc)

    # 搜索教练并选择
    def sel_coach(self, coach_name):
        self.type_text(coach_name, *self.search_coach_name_loc)
        time.sleep(1)
        self.click(*self.search_btn_loc)
        time.sleep(2)
        self.click(*self.sel_coach_loc)
        time.sleep(1)
        self.click(*self.sel_save_btn_loc)

    # 获取已选教练名称
    def get_coach_name(self):
        return self.get_text(*self.sel_coach_name_loc)

    # 保存排课并返回结果文案
    def save_course(self):
        self.click(*self.save_btn_loc)
        time.sleep(2)
        return self.get_text(*self.result_text_loc)

    # 查询出指定的排课
    def query_course(self, begin_date, end_date, company_name=''):
        if company_name:
            self.sel_company(company_name)
        else:
            pass
        self.type_query_begin_date(begin_date)
        self.type_query_end_date(end_date)
        self.click_query_btn()

    # 点击编辑按钮
    def click_edit_btn(self):
        self.click(*self.edit_btn_loc)

    # 获取排课月份
    def get_course_month(self):
        return self.get_value(*self.month_loc)

    # 勾选隐藏已选课班级
    def click_hide_class(self):
        self.click(*self.hide_btn_loc)

    # 选择要复制几月份的排课
    def sel_copy_month(self, date):
        self.type_value_by_id('month2', date)

    # 点击复制按钮
    def click_copy_btn(self):
        jq = "$('input.copy').removeAttr('disabled');"
        self.execute_script(jq)
        self.click(*self.copy_btn_loc)

    # 点击确定按钮
    def click_copy_ok_btn(self):
        self.click(*self.copy_ok_loc)

    # 复制排课
    def copy_course(self, will_date, copy_date):
        self.sel_month(will_date)
        time.sleep(4)
        self.click_copy_btn()
        time.sleep(2)
        self.sel_copy_month(copy_date)
        time.sleep(2)
        self.click_copy_ok_btn()
        time.sleep(2)

    # 返回弹窗文案
    def get_result_text(self):
        return self.get_text(*self.result_text_loc)

    # 点击查看按钮
    def click_look_btn(self):
        self.click(*self.look_btn_loc)

    # 获取查看窗口标题文字
    def get_text_of_look(self):
        return self.get_text(*self.look_title_loc)

if __name__ == '__main__':
    pass

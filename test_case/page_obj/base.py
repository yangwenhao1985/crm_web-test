from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class Page(object):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url  # 初始化URL

    # 打开URL
    def open_url(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    # 关闭浏览器
    def close(self):
        self.driver.quit()

    # 获取元素
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    # 获取一组元素
    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    # 点击
    def click(self, *loc):
        self.driver.find_element(*loc).click()

    # 获取当前页面的Title
    def get_title(self):
        return self.driver.title

    # 输入
    def type_text(self, text, *loc):
        self.driver.find_element(*loc).clear()
        self.driver.find_element(*loc).send_keys(text)

    def type_value_by_id(self, ele_id, value):
        """
        根据元素的ID，使用jQuery代码给元素赋值；
        此方法适用于那些不能直接使用selenium方法定位并赋值的元素，例如日期控件
        :param ele_id: 元素的ID
        :param value: 要输入的值
        :return: 无返回值
        """
        jq = "$('#" + ele_id + "').val('" + value + "')"
        self.driver.execute_script(jq)

    def type_value_by_class_name(self, ele_class_name, value):
        """
        根据元素的className，使用jQuery代码给元素赋值；
        此方法适用于那些不能直接使用selenium方法定位并赋值的元素，例如日期控件
        :param ele_class_name: 元素的className
        :param value: 要输入的值
        :return: 无返回值
        """
        jq = "$('." + ele_class_name + "').val('" + value + "')"
        self.driver.execute_script(jq)

    def sel_value(self, value, *loc):
        """
        元素为下拉菜单时，从中选择指定值
        :param value: 要选择数据
        :param loc: 元素定位
        :return: 无返回值
        """
        sel = Select(self.driver.find_element(*loc))
        sel.select_by_visible_text(value)

    def get_text(self, *loc):
        """
        获取元素的text值
        :param loc: 元素定位 （{By.ID, 'test'}）
        :return: 元素的text值
        """
        return self.driver.find_element(*loc).text

    def get_value(self, *loc):
        """
        获取元素的value属性值
        :param loc: 元素定位 （{By.ID, 'test'}）
        :return: 元素的value属性值
        """
        return self.driver.find_element(*loc).get_attribute("value")

    def execute_script(self, jq):
        """
        执行JavaScript命令
        :param jq: JavaScript或jquery代码
        :return: 无返回值
        """
        self.driver.execute_script(jq)

    def scroll_target(self, *loc):
        target = self.driver.find_element(*loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def get_look_results_dic(self, *loc):
        """
        获取查看详情页的字段名和值组成字典返回。
        :param loc: 元素定位
        :return: 字典，例如：{"姓名"："刘红育"}
        """
        labels_ele = self.find_elements(*loc[0])
        values_ele = self.find_elements(*loc[1])
        values_ele.insert(3, self.find_element(*loc[2]))
        data_dic = {}
        for name, ele in zip(labels_ele, values_ele):
            key = name.text
            value = ele.get_attribute("value")
            if key == '性别:':
                if ele.is_selected():
                    value = '男'
                else:
                    value = '女'
            data_dic[key] = value
        return data_dic

    def get_results_dic(self, *loc):
        """
        获取查询结果表头和字段值对应的字典
        :param loc: 表头所有td元素的定位和表中某一行所有td元素的定位
        :return: 字典，例如：{"姓名"："刘红育"}
        """
        titles = self.find_elements(*loc[0])
        elements = self.find_elements(*loc[1])
        data_dic = {}
        for name, ele in zip(titles, elements):
            title = name.text
            if title.find("状态") != -1:
                title = "status"
            value = ele.text
            data_dic[title] = value
        return data_dic

    def is_element_visible(self, element):
        """
        判断元素是否可见
        :param element: 元素定位
        :return: 布尔值，TRUE 或者 FALSE
        """
        try:
            the_element = EC.visibility_of_element_located(element)
            assert the_element(self.driver)
            flag = True
        except:
            flag = False
        return flag

    # 切换window
    def switch_window(self):
        current_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)

    def get_list_num(self, *loc):
        """
        获取列表的行数
        :param loc: 元素定位（根据该定位获取一组元素）
        :return: int格式的行数
        """
        return len(self.driver.find_elements(*loc))

    # 获取页码
    def get_page_num(self):
        return self.driver.find_element(By.ID, 'total').get_attribute('value')

    # 点击下一页
    def click_next_page(self):
        self.driver.find_element(By.XPATH, "//input[@value='下一页']").click()


if __name__ == "__main__":
    pass

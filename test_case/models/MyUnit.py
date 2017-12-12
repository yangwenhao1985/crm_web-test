import unittest
import time
import config
import threading
from selenium import webdriver
from test_case.page_obj import *
from threading import Thread


class MyLoginTest(unittest.TestCase):
    def setUp(self):
        self.url = config.get_config('env', 'url')  # 从配置文件获取初始URL
        self.browser = config.get_config('driver', 'browser_name')  # 从配置文件获取要使用的浏览器
        if self.browser == 'Firefox':
            self.driver = webdriver.Firefox()
        elif self.browser == 'Chrome':
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            self.driver = webdriver.Chrome(chrome_options=options)
        elif self.browser == 'IE':
            self.driver = webdriver.Ie()
        else:
            self.driver = webdriver.Firefox()
        self.driver.get(self.url)
        self.driver.maximize_window()  # 最大化窗口

    def tearDown(self):
        self.driver.quit()


class MyTestOne(unittest.TestCase):
    """
    封装了setUpClass和tearDownClass方法 。
    """
    driver_dict = {}  # 声明一个浏览器驱动的字典变量
    driver_type = config.get_config('driver', 'driver_type')  # 从配置文件获取浏览器驱动类型(remote or local)
    username = config.get_config('login', 'username')  # 从配置文件获取登录用户的名称
    url = config.get_config('env', 'url')  # 从配置文件获取初始URL

    @staticmethod
    def get_host_browser(driver_type):
        """
        获取浏览器配置
        remote：按照线程返回配置文件中编写的host和浏览器名称
        local：返回配置文件中设置的浏览器名称，host写死等于local
        :param driver_type: 浏览器驱动类型，在配置文件中设置（remote or local）
        :return: host 和 浏览器名称
        """
        host = ''
        browser = ''
        if driver_type == 'remote':
            dr = eval(config.get_config('driver', 'browser_list'))  # 从配置文件获取驱动列表
            thread_name = threading.current_thread().name  # 获取当前运行的线程名称
            index = int(thread_name.split('-')[1]) - 1  # 获取对应每个线程的int型的数字
            drivers = dr[index]
            for _host, _browser in drivers.items():
                host = _host
                browser = _browser
        elif driver_type == 'local':
            browser = config.get_config('driver', 'browser_name')
            host = 'local'
        else:
            print("驱动类型错误，请检查配置文件！")
        return host, browser  # 返回

    @staticmethod
    def get_driver(driver_type, host, browser):

        dr = {}
        if driver_type == 'remote':
            dc = {'browserName': browser}  # 拼接dc
            dr[host] = webdriver.Remote(command_executor=host,
                                        desired_capabilities=dc)
        elif driver_type == 'local':
            if browser == 'Firefox':
                driver = webdriver.Firefox()
            elif browser == 'Chrome':
                driver = webdriver.Chrome()
            elif browser == 'Ie':
                driver = webdriver.Ie()
            elif browser == 'Edge':
                driver = webdriver.Edge()
            else:
                driver = webdriver.Firefox()
            dr[host] = driver
        else:
            print("驱动类型错误，请检查配置文件！")
        return dr[host]

    @staticmethod
    def init_login(driver, url):

        user_phone = config.get_config('login', 'user_phone')  # 从配置文件获取登录用户的手机号
        pwd = config.get_config('login', 'pwd')  # 从配置文件获取登录用户的密码
        login_page = login_manage_page.LoginManagePage(driver, url)
        login_page.user_login(user_phone, pwd)

    @classmethod
    def setUpClass(cls):
        """
        每个测试类执行前都会执行的方法。
        完成打开浏览器并登录操作。
        :return: None
        """
        (host, browser) = cls.get_host_browser(cls.driver_type)
        cls.driver_dict[host] = cls.get_driver(cls.driver_type, host, browser)
        cls.init_login(cls.driver_dict[host], cls.url)

    @classmethod
    def tearDownClass(cls):
        (host, browser) = cls.get_host_browser(cls.driver_type)
        cls.driver_dict[host].quit()

    def setUp(self):
        (host, browser) = self.get_host_browser(self.driver_type)
        self.driver = self.driver_dict[host]
        self.operation_page = self.get_page_instance()
        self.user_page = user_manage_page.UserManagePage(self.driver, self.url)

    def get_page_instance(self):
        """
        创建当前测试模块对应的page实例
        :return: page object 实例
        """
        module_name = self.__module__  # 获取当前模块的名称，例如：call_manage_test
        prefix = module_name.split('_test')[0]  # 获取模块名称的前缀，例如：call_manage
        page_module_name = prefix + '_page'  # 拼接Page对象的模块名称，例如：call_manage_page
        tmp_name_list = prefix.split('_')  # 将测试模块的前缀按照下划线分割
        class_name_prefix = ''  # 定义一个变量
        for name in tmp_name_list:  # 循环遍历测试模块的前缀，然后将每个单词首字母大写后拼接，结果例如：CallManage
            class_name_prefix += name.capitalize()
        page_class_name = class_name_prefix + 'Page'  # 拼接处Page对象的类名称，例如：CallManagePage
        # 拼接一个创建Page对象实例的字符串，例如：call_manage_page.CallManagePage(self.driver, self.url)
        page_instance_str = page_module_name + '.' + page_class_name + '(self.driver, self.url)'
        return eval(page_instance_str)  # 返回eval后的实例

    # 翻页测试用例
    def turn_page_test(self, page_obj):
        page_lis1 = page_obj.get_page_num().split("/")
        cur_page1 = page_lis1[0]
        total_page1 = page_lis1[1]
        if total_page1 > cur_page1:
            page_obj.click_next_page()
            time.sleep(2)
            page_lis2 = page_obj.get_page_num().split("/")
            self.assertEqual(int(cur_page1) + 1, int(page_lis2[0]))
        else:
            self.fail("只有一页数据")


if __name__ == '__main__':
    pass

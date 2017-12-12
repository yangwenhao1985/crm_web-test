import os
import time
import unittest
import config
from threading import Thread
from package import HTMLTestRunner
from test_case.models.MyUnit import MyTestOne

__author__ = 'Sixmiaomiao'


def suite():
    """
    获取TestCase组成TestSuite返回。
    :return: TestSuite
    """
    loader = unittest.TestLoader()
    case_path = config.get_config('directory', 'case_path')  # 从配置文件获取TestCase存放的目录
    suite1 = loader.discover(case_path, pattern='course_*_test.py')
    return suite1


def run_test(report_path):
    """
    执行测试用例并生成测试报告
    :param report_path: 测试报告存放路径
    :return:
    """
    # 定义测试报告
    with open(report_path, 'wb') as report:
        runner = HTMLTestRunner.HTMLTestRunner(stream=report,
                                               title="宏远云管理后台自动化测试报告",
                                               description="用例执行情况")
        # 运行测试用例
        runner.run(suite())


def single_run():
    """
    使用本地浏览器单一运行测试用例
    :return:
    """
    browser = config.get_config('driver', 'browser_name')  # 从配置文件获取浏览器配置
    report_path = get_report_path(browser)  # 获取测试报告存放路径
    run_test(report_path)  # 调用运行测试用例方法


def get_report_path(browser):
    """
    生成测试报告存放路径
    :param browser: 浏览器名称
    :return: 测试报告路径字符串
    """
    time_now = time.strftime("%Y-%m-%d-%H-%M")  # 获取当前时间并格式化
    path = config.get_config('directory', 'report')  # 从配置文件获取存放report的目录

    # 定义报告文件路径和名字，路径为项目下的report目录，名字是report+当前时间拼接而成（可自定义），格式为.html
    report_path = path + 'report_' + time_now + '_' + browser + ".html"

    # 判断是否定义的路径目录存在，不能存在则创建
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass
    return report_path


def multiple_run():
    """
    使用Selenium grid工具，并行运行测试用例
    :return:
    """
    dr_list = eval(config.get_config('driver', 'browser_list'))  # 从配置文件获取浏览器配置
    threads = []  # 创建线程组
    files = range(len(dr_list))
    (host, browser) = MyTestOne.get_host_browser('remote')  # 获取当前线程使用的浏览器名称，例如：Chrome
    report_path = get_report_path(browser)  # 获取测试报告存放路径
    for i in files:
        t = Thread(target=run_test, args=(report_path,))  # 创建线程
        threads.append(t)  # 把线程加入线程列表中
        threads[i].start()  # 启动线程

    for i in files:
        threads[i].join()  # 等待线程


def main_run(driver_type):
    """
    执行测试用例入口
    :param driver_type: 驱动类型，（remote or local）
    :return:
    """
    if driver_type == 'local':
        single_run()
    elif driver_type == 'remote':
        multiple_run()
    else:
        print("浏览器驱动类型错误，请检查配置文件中，section name 为[driver]的块！")

if __name__ == '__main__':
    dr_type = config.get_config('driver', 'driver_type')
    main_run(dr_type)

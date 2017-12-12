import xlrd
import xlwt
import os
import time
import config

__author__ = 'Sixmiaomiao'


def screen_shot(driver, pic):
    """
    截图方法
    :param driver: selenium webdriver
    :param pic: 图片名称.png
    :return: None
    """

    pic_path = config.get_config('directory', 'screenshot')  # 指定截图存储的路径
    if not os.path.exists(pic_path):  # 判断该路径是否存
        os.mkdir(pic_path)  # 路径不存在，创建路径
    else:
        pass
    time1 = time.strftime("%Y-%m-%d-%H-%M")
    pic_name = pic_path + time1 + pic  # 拼接截图的路径和名称
    driver.save_screenshot(pic_name)  # 调用webdriver的截图功能


def write_kaoqin(lis):
    work_book = xlwt.Workbook()
    work_sheet = work_book.add_sheet("kaoqin")
    for i in range(len(lis)):
        row_values = lis[i]
        for j in range(len(row_values)):
            work_sheet.write(i, j, row_values[j])
    work_book.save('kaoqin.xls')

def read_kaoqin(data_type, sheet_name, num):
    """
    读取Excel数据
    :param data_type: 数据类型，（例如：USER）
    :param sheet_name: 数据类型，（例如：USER）
    :return: 数据list（例如：[("jack", 13, "男"), ("rose", 12, "女")]）
    """
    excel_path = config.get_config('data', data_type)
    with xlrd.open_workbook(excel_path) as data:  # 调用xlrd模块的方法打开Excel文件，命名为data
        table = data.sheet_by_name(sheet_name)  # 根据sheet页名称获取sheet页内容
        print(table)
        listA = []
        name = ''
        for i in range(num, 10):
            user_name = table.cell_value(i, 2)
            if i == num:
                name = table.cell_value(num, 2)
                listA.append(table.row_values(i))
            elif user_name == name:
                listA.append(table.row_values(i))
            else:
                break
        return listA
        rows_num = table.nrows  # 获取行数
        print(rows_num)
        re_list = []  # 创建一个list
        dict = {}
        user_names = []
        for row_num in range(1, rows_num):  # 遍历行数

            user_name = table.cell_value(row_num, 2)
            user_names.append(user_name)
            row = table.row_values(row_num)  # 获取每行数据
            re_list.append(row)  # 将Tuple加入到list中
            # print(row)
            # tup = tuple(row)  # 将遍历出来的数据list转换为元组Tuple

        dict[user_name] = re_list
        print(dict)
        return re_list

def read_excel1(data_type, sheet_name):
    """
    读取Excel数据
    :param data_type: 数据类型，（例如：USER）
    :param sheet_name: 数据类型，（例如：USER）
    :return: 数据list（例如：[("jack", 13, "男"), ("rose", 12, "女")]）
    """
    excel_path = config.get_config('data', data_type)
    with xlrd.open_workbook(excel_path) as data:  # 调用xlrd模块的方法打开Excel文件，命名为data
        table = data.sheet_by_name(sheet_name)  # 根据sheet页名称获取sheet页内容
        rows_num = table.nrows  # 获取行数
        re_list = []  # 创建一个list
        for row_num in range(1, rows_num):  # 遍历行数
            row = table.row_values(row_num)  # 获取每行数据
            tup = tuple(row)  # 将遍历出来的数据list转换为元组Tuple
            re_list.append(tup)  # 将Tuple加入到list中
        return re_list


def read_excel(sheet_name, table_name, excel_name='test_data'):
    """
    读取Excel数据
    :param sheet_name: sheet页名称，（例如：call）
    :param table_name: 合并单元格的名称，（例如：query_call）
    :param excel_name: Excel表名,这是在config.ini文件中配置的，（例如：test_data）
    :return: 数据list（例如：[("jack", 13, "男"), ("rose", 12, "女")]）
    """
    excel_path = config.get_config('data', excel_name)
    with xlrd.open_workbook(excel_path) as data:  # 调用xlrd模块的方法打开Excel文件，命名为data
        sheet = data.sheet_by_name(sheet_name)  # 根据sheet页名称获取sheet页内容
        rows_num = []
        head_row = []
        re_list = []  # 创建一个list
        col = 0
        for (r_low, r_high, c_low, c_high) in sheet.merged_cells:
            if sheet.cell_value(r_low, c_low) == table_name:
                rows_num = range(r_low+1, r_high)
                head_row = sheet.row_values(r_low)
                break
        for cell_val in head_row:
            if cell_val == '':
                break
            col += 1
        for row_num in rows_num:  # 遍历行数
            row = sheet.row_values(row_num, start_colx=1, end_colx=col)  # 获取每行数据
            tup = tuple(row)  # 将遍历出来的数据list转换为元组Tuple
            re_list.append(tup)  # 将Tuple加入到list中
        return re_list


if __name__ == '__main__':
    # read_kaoqin('kaoqin_data', 'Sheet1', 3)
    write_kaoqin(read_kaoqin('kaoqin_data', 'Sheet1', 3))

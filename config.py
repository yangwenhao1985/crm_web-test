import configparser
import os


def get_config(sec_name, key_name):
    """ 获取配置数据 """
    cfg = configparser.ConfigParser()   # 创建读取配置文件的对象
    fl = __file__
    real = os.path.realpath(__file__)
    path = os.path.split(os.path.realpath(__file__))[0] + '/config.ini'     # 获取当前文件的路径

    cfg.read(path)  # 调用read方法读取配置文件
    print(cfg.sections())
    if sec_name in cfg.sections() and key_name in cfg.options(sec_name):
        return cfg.get(sec_name, key_name)
    else:
        return None


def get_options(sec_name):
    cfg = configparser.ConfigParser()  # 创建读取配置文件的对象
    path = os.path.split(os.path.realpath(__file__))[0] + '/config.ini'  # 获取当前文件的路径

    cfg.read(path)  # 调用read方法读取配置文件
    if sec_name in cfg.sections():
        return cfg.options(sec_name)
    else:
        return None


if __name__ == '__main__':
    print(get_config("env", "url"))

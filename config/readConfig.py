import os
from configparser import ConfigParser
from configobj import ConfigObj
curPath = os.path.abspath(os.path.dirname(__file__))
config = ConfigParser()
rootPath = os.path.abspath(os.path.split(os.path.abspath(os.path.realpath(__file__)))[0] + "/../")
config_path = rootPath + '/config/config.ini'
config.read(config_path, encoding='utf-8')

class ReadConfig:


    @staticmethod
    def get_Account(key):
        result = config.get('ACCOUNT', key)
        return result


class WriteConfig:
    # 写配置文件
    @staticmethod
    def update_Config(module, key, value):
        config1 = ConfigObj(config_path, encoding='UTF8')
        config1[module][key] = value
        config1.write()
        config.read(config_path, encoding='utf-8')


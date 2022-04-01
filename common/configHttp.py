import json
import requests
from urllib import parse
from common.Log import logger
import urllib.parse
import unittest
import os
from configparser import ConfigParser

logger = logger

def url_join_args(api, query):
    result = api + "?" + urllib.parse.urlencode(query)
    return result

def read_again():
    config.read(config_path, encoding='utf-8')


curPath = os.path.abspath(os.path.dirname(__file__))
config = ConfigParser()
rootPath = os.path.abspath(os.path.split(os.path.abspath(os.path.realpath(__file__)))[0] + "/../")
config_path = rootPath + '/config/config.ini'
config.read(config_path, encoding='utf-8')

phone = config.get('ACCOUNT', 'pre-phone')


# 封装HTTP请求
class RunMain(unittest.TestCase):

    @staticmethod
    def send_post(url, data, header=None):
        # 不带自定义header
        if header == None:
            headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8', }
        else:
            headers = header
        result = requests.post(url=url, json=data, headers=headers).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True)
        return res

    @staticmethod
    def send_get(url, data, header=None):
        if header == None:
            headers = {'Content-Type': 'application/json;charset=utf-8', }
        else:
            headers = header
        result = requests.get(url=url, json=data, headers=headers).json()
        return result

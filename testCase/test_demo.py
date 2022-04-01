#!/usr/bin/python
# encoding=utf-8

"""
@Author  :  SunPeng
@Date    :  2022/3/10 12:30 下午
@Desc    :
"""
import unittest
import common.Log
from common import configHttp
log = common.Log.logger
http_request=configHttp.RunMain()

class TestDemo(unittest.TestCase):

    def test_get_data(self):
        result=http_request.send_get('http://httpbin.org/get',None,None)
        unittest.TestCase.assertEqual(self, result.get('url'),'http://httpbin.org/get')
        print("请求成功！")



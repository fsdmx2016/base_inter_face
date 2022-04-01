#!/usr/bin/python
# encoding=utf-8

"""
@Author  :  SunPeng
@Date    :  2022/3/10 12:36 下午
@Desc    :
"""
from common import configHttp
from config import readConfig

import common.Log

log = common.Log.logger
request = configHttp.RunMain()
base_url = readConfig.config.get('ACCOUNT', 'base_url')


class Interface_Base:
    @staticmethod
    def interface_base_demo(id: str, name: str):
        url = base_url + 'XXX'
        data = {
            "id": id,
            "name": name,
        }
        result = request.send_post(url, data)
        log.info("请求结果" + result)
        return result

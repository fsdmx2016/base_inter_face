import os
import unittest

from result import HTMLTestRunner
import common.Log
import time
import logging

log = common.Log.logger
path = os.path.abspath(os.path.dirname(__file__)) + '/testCase'
def runTestSuite():
    suit = unittest.TestSuite()
    case_list = []
    for root_dir, dir_list, fileName in os.walk(path):
        for file in fileName:
            if file.endswith(".py") and not file.startswith("__"):
                case_list.append(file)
    for case in case_list:
        discover = unittest.defaultTestLoader.discover(start_dir=path, pattern=case)
        suit.addTest(discover)
    return suit


if __name__ == '__main__':
    # clear_dirty_data.ClearOrgDirtyData.clear_data()
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    curPath = os.path.abspath(os.path.dirname(__file__))
    filename = curPath + "/result/" + now + "_result.html"
    fp = open(filename, 'wb')
    # 测试报告输出方式
    logger = logging.getLogger('demos')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'接口自动化测试报告',
        description=u'用例执行情况：', verbosity=2)
    runner.run(runTestSuite())

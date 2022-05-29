import unittest
import platform
import os.path
import logging
from common.HTMLTestRunnerCNs import HTMLTestRunner
class RunCase(object):
    report_dir = "../reports"

    # 执行用例函数
    def run_case(self):
        # 运行测试用例并生成html测试报告
        with open('{}//et_result.html'.format(self.report_dir), 'wb') as fp:

            try:
                logging.info("RunCase执行用例--开始")
                suite = unittest.TestSuite()
                tests = unittest.defaultTestLoader.discover('..\\test_case', pattern='test*')
                suite.addTest(tests)
                runner = HTMLTestRunner(stream=fp, title=u'通讯录APP自动化测试报告', description=u'运行环境：{}'.format(platform.platform()),
                                        tester="i东方不败")
                runner.run(suite)
                logging.info("RunCase执行用例--结束")
            except Exception as e:
                logging.error("RunCase执行用例，生成报告失败：{}".format(e))


if __name__ == '__main__':
    test = RunCase()  # 创建对象
    test.run_case()  # 调用测试用例执行函数

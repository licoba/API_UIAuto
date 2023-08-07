# app_ui_autotest
APP移动端UI自动化 unittest+appium+HTMLTestRunner

run执行入口，收集用例->执行test_login，测试类TestAdd继承StartEnd->执行StartEnd的setup，进行driver设置->执行test_login 下的test_get_zhangsan->
执行StartEnd中的teardown
->执行StartEnd的setup>执行test_login下的test_login_001->执行StartEnd中的teardown->生成测试报告

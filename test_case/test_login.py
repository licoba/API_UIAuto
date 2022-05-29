import unittest
import logging
from common.myunit import StartEnd
from businessView.loginView import LoginView
class TestAdd(StartEnd):
    csv_file='../data/account.csv'
    def test_login_001(self):
        logging.info("---------------test_login_001---------------")
        l=LoginView(self.driver)
        data=l.get_csv_data(self.csv_file,1)
        e=l.add_account(data[0],data[1])
        print("获取到的值:"+e)

        self.assertEqual(e,data[0])#对比获取到的name和传入的name


    def test_get_zhangsan(self):
        l = LoginView(self.driver)
        e=l.get_zhangsan()
        self.assertEqual(e,"张三")


if __name__ == '__main__':
    unittest.main()


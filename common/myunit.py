import unittest
from common.desired_caps import appium_desired
import logging
from time import sleep
class StartEnd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.info("---------------setup-------------")
        cls.driver=appium_desired()
    @classmethod
    def tearDownClass(cls):
        logging.info("---------------tearDown---------")
        sleep(5)
        # self.driver.close_app()

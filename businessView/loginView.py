import logging
from common.common_fun import Common,NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
class LoginView(Common):
    user_input=(By.NAME,"姓名") #姓名输入框
    phone_input=(By.NAME,"电话")  #电话输入框
    check_button=(By.ID,"com.android.contacts:id/menu_save")
    name_button=(By.ID,"com.android.contacts:id/large_title")#创建账号后的姓名元素
    zhangsan_text=(By.ID,"com.android.contacts:id/cliv_name_textview")
    def add_account(self,username,phone):
        "添加账号流程"
        self.check_addbutton()
        logging.info("-----------添加账号操作-----------")
        self.driver.find_element(*self.user_input).send_keys(username)
        self.driver.find_element(*self.phone_input).send_keys(phone)
        self.driver.find_element(*self.check_button).click()
        e=self.driver.find_element(*self.name_button).text
        return e
    def get_zhangsan(self):
        e = self.driver.find_element(*self.zhangsan_text).text
        return e








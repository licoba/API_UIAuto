import logging

from appium.webdriver.common.appiumby import AppiumBy

from common.common_fun import Common, NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By


class LoginView(Common):
    user_inputs = (By.CLASS_NAME, "android.widget.EditText")  # 姓氏、名字输入框，不同的Android系统也不同，找到所有的输入框
    # phone_input = (By.NAME, "电话")  # 电话输入框
    phone_input = (By.XPATH, "//android.widget.EditText[@text='电话']")  # 电话输入框
    # save_button = (By.ID, "com.android.contacts:id/menu_save")  # 保存按钮
    save_button = (By.XPATH, "//android.widget.Button[@text='保存']")  # 保存按钮
    name_text = (By.ID, "com.android.contacts:id/large_title")  # 创建账号后的姓名元素
    all_text = (By.CLASS_NAME, "android.widget.TextView")
    zhangsan_text = (By.ID, "com.android.contacts:id/cliv_name_textview")

    def add_account(self, username, phone):
        """添加账号流程"""
        self.check_addbutton()
        print("\n-----------现在来到了添加输入界面，即将进行添加账号操作-----------")
        inputs = self.driver.find_elements(*self.user_inputs)
        inputs[0].send_keys(username)  # 向第一个输入框内输入文字
        self.driver.find_element(*self.phone_input).send_keys(phone)
        self.driver.implicitly_wait(1)
        self.driver.find_element(*self.save_button).click()
        self.driver.implicitly_wait(1)
        print("-----------获取姓名元素-----------")
        # results = self.driver.find_element(*self.all_text)
        # e = results[-1].text
        textview = self.driver.find_element(AppiumBy.ID, "large_title")
        e = textview.text
        print("-----------获取到了姓名元素-----------", e)
        return e

    def get_zhangsan(self):
        e = self.driver.find_element(*self.zhangsan_text).text
        return e

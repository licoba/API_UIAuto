import csv
import logging
import os.path
import time

from baseView.baseView import BaseView
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class Common(BaseView):
    addbutton=(By.ID,"com.android.contacts:id/floating_action_button")#添加账户按钮
    check_button=(By.ID,"com.android.contacts:id/left_button")
    csv_file=''
    def check_addbutton(self):
        "检测是否有添加账号按钮"
        logging.info("================check_addbutton=============")
        # try:
        #     addbutton=self.driver.find_element(*self.addbutton)
        #     check_button=self.driver.find_element(*self.check_button)
        # except NoSuchElementException:
        #     logging.info("没有添加按钮")
        # else:
        #     addbutton.click()
        #     check_button.click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.addbutton).click()  # 点击添加账户按钮
        self.driver.find_element(*self.check_button).click()#点击本地保存按钮 这里定位不到不知道什么原因





    def get_size(self):
        x=self.driver.get_windows_size()['width']
        y=self.driver.get_windows_size()['height']
        return  x,y

    def swipe(self):
        logging.info("左滑")
        l=self.get_size()
        x1=int(l[0]+0.9)
        x2=int(l[0]+-0.2)
        y1=int(l[1]+0.5)
        self.swipe(x1,y1,x2,y1,1000)

    def getTime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")
        return  self.now

    def getScreenShot(self,modult):
        time=self.getTime()
        image_file=os.path.dirname()

    def get_csv_data(self,csv_file,line):
        logging.info("---获取测试数据---")
        with open(csv_file,'r',encoding='utf-8')as file:
            reader=csv.reader(file)
            for index,row in enumerate(reader,1):
                if index==line:
                    return row


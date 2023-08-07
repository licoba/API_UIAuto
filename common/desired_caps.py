from appium import webdriver
import yaml

import logging
import logging.config
import os
CON_LOG='../config/log/conf'


def appium_desired():
    """
    yaml是一种简洁的非标记语言，以数据为中心，使用空白，分行组织数据
    :return:
    """
    with open('../config/config.yaml','r',encoding='utf-8')as file:
        data=yaml.load(file, Loader=yaml.FullLoader)
    #创建设备信息
    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=data['platformVersion'] # #在手机设置，关于平板电脑可以找到版本
    desired_caps['deviceName']=data['deviceName'] #模拟器上设备的名称 在cmd下用adb devices显示的地址
    desired_caps['appPackage']=data['appPackage']#通讯录包名
    desired_caps['appActivity']=data['appActivity']#app活动名

    #连接
    driver=webdriver.Remote(data['url'],desired_caps)#连接的是appium
    driver.implicitly_wait(5)

    # #定位
    # driver.find_element_by_id("com.android.contacts:id/floating_action_button").click() #点击添加账号按钮
    return driver






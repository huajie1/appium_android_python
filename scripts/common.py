# encoding: utf-8

import os
from selenium.webdriver.support.ui import WebDriverWait


# 第六次课：点击手机屏幕的某个位置
def click_by_adb(x, y):
    print "Start tap anypoint point"
    # cmd = "adb shell input tap"+" "+str(x)+" "+str(y)
    cmd = 'adb shell input tap {} {}'.format(x, y)
    # print ('excute command >>>{}'.format(cmd))
    os.popen(cmd)


# 通过文本点击定位并点击某个元素
def click_el_by_text(self, text):
    print "start find element by uiautomator text"
    el = self.driver.find_element_by_android_uiautomator('new UiSelector().text("{}")'.format(text))
    el.click()


# 第十次课:封装向左、向右滑动
# 实现从手机屏幕3/4向左滑动到1/4处
def swipe_left(self):
    print "start swipe left"
    # 获取手机屏幕的宽、高
    width = self.driver.get_window_size()['width']
    height = self.driver.get_window_size()['height']
    self.driver.swipe(width*4/5, height/2, width*1/5, height/2, 1000)


# 实现从手机屏幕1/4向右滑动到3/4
def swipe_right(self):
    print "start swipe right"
    # 获取手机屏幕的宽、高
    width = self.driver.get_window_size()['width']
    height = self.driver.get_window_size()['height']
    self.driver.swipe(width*1/5, height/2, width*4/5, height/2, 1000)


# 第十二次课:等待某个元素出现
def wait_appear_by_id(self, id, timeout):
    print "wait element appear"
    WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element_by_id(id), "E\元素未出现")


def wait_appear_by_class_name(self, class_name, timeout):
    print "wait element appear"
    WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element_by_class_name(class_name), "E\元素未出现")


def wait_appear_by_xpath(self, xpath, timeout):
    print "wait element appear"
    WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element_by_xpath(xpath), "E\元素未出现")


def wait_appear_by_name(self, name, timeout):
    print "wait element appear"
    WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element_by_name(name), "E\元素未出现")


# 第十二次课:等待某个元素消失
def wait_disappear_by_id(self, id, timeout):
    print "wait element appear"
    WebDriverWait(self.driver, timeout).until_not(lambda driver: driver.find_element_by_id(id), "E\元素未消失")

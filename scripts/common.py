# encoding: utf-8

# 第六次课：点击手机屏幕的某个位置
import os


def click_by_adb(x, y):
    print "Start tap anypoint point"
    # cmd = "adb shell input tap"+" "+str(x)+" "+str(y)
    cmd = 'adb shell input tap {} {}'.format(x, y)
    # print ('excute command >>>{}'.format(cmd))
    os.popen(cmd)


def click_el_by_text(self, text):
    print "start find element by uiautomator text"
    el = self.driver.find_element_by_android_uiautomator('new UiSelector().text("{}")'.format(text))
    el.click()


# 第十次课:封装向左、向右滑动
# 实现从手机屏幕3/4向左滑动到1/4处
def swipe_left(self):
    print "start swipe left"
    width = self.driver.get_window_size()['width']
    height = self.driver.get_window_size()['height']
    self.driver.swipe(width*3/4, height/2, width*1/4, height/2, 1000)


# 实现从手机屏幕1/4向右滑动到3/4
def swipe_right(self):
    print "start swipe right"
    width = self.driver.get_window_size()['width']
    height = self.driver.get_window_size()['height']
    self.driver.swipe(width*1/4, height/2, width*3/4, height/2, 1000)

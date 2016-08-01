# encoding: utf-8
import os
import unittest
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


#  使用appium提供的testapp实现手势密码解锁
class TestUnlock(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '三星S6 Edge'
        desired_caps['app'] = PATH('../app/MobileOffice.apk')
        desired_caps['appPackage'] = 'com.paic.mo.client'
        desired_caps['appActivity'] = 'com.paic.mo.client.activity.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(60)

    def tearDown(self):
        self.driver.quit()

    # 启动页三页向左滑动三次至登录界面,调用向左滑动公共方法
    def test_unlock(self):
        print "start"
        self.driver.find_element_by_id("com.paic.mo.client:id/pattern_to_login").click()
        action = TouchAction(self.driver)
        sleep(5)
        # 道理一样,就只写两个点了,用的test app的手势密码区域是一整张图片,只能使用坐标进行点击,效果见截图
        action.press(x=298, y=1034).wait(5000).move_to(x=719, y=1034).release().perform()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUnlock)
    unittest.TextTestRunner(verbosity=2).run(suite)

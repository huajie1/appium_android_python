# encoding: utf-8
import os
import unittest
from appium import webdriver
from time import sleep
import common

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestLogin(unittest.TestCase):
    def setUp(self):
        desired_caps = {}

        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '三星S6 Edge'

        # PATXT
        desired_caps['app'] = PATH('../app/txt_test.apk')
        desired_caps['appPackage'] = 'com.pingan.wetalk'
        desired_caps['appActivity'] = 'com.pingan.wetalk.module.splash.activity.SplashActivity'

        # PASDK
        # desired_caps['app'] = PATH('../app/PASDK.apk')
        # desired_caps['appPackage'] = 'com.pingan.imui'
        # desired_caps['appActivity'] = 'com.pingan.imui.SplashActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(60)

    def tearDown(self):
        self.driver.quit()

    # 启动页三页向左滑动三次至登录界面,调用向左滑动公共方法
    def test_login_txt(self):
        print "start launching txt"
        sleep(5)
        title = self.driver.find_element_by_class_name("android.widget.ImageView")
        title.is_displayed()
        common.swipe_left(self)
        sleep(3)
        common.swipe_left(self)
        sleep(3)
        common.swipe_left(self)
'''
    # 实现登录
    def test_login_sdkdemo(self):
        print "start login sdk"
        sleep(5)
        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys("18888888888")
        self.driver.hide_keyboard()
        common.click_el_by_text(self, "登录")
        # self.driver.find_element_by_name("登录").click()
        sleep(30)
'''

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    unittest.TextTestRunner(verbosity=2).run(suite)

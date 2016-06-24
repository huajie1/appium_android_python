# encoding: utf-8
import os
import unittest
from appium import webdriver
from time import sleep

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
        desired_caps['app'] = PATH('../app/PASDK.apk')
        desired_caps['appPackage'] = 'com.pingan.imui'
        desired_caps['appActivity'] = 'com.pingan.imui.SplashActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        print "start launching"
        textfields =  self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys("18888888888")
        self.driver.hide_keyboard()
        self.driver.find_element_by_name("登录").click()
        sleep(30)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    unittest.TextTestRunner(verbosity=2).run(suite)

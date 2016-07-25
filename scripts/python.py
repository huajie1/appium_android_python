# encoding: utf-8
import os
import time

import common


# 第二节课1:检测是否安装某应用,如果安装输出路径,否则执行安装
def get_path():
    print "Start get app path..."
    # 列出所有的安装包
    packages = os.popen("adb shell pm list packages").read()
    # 本地包路径
    path = "/Users/huajie/Desktop/txt_test.apk"
    if packages.find("com.pingan.wetalk") != -1:
        # 输出包路径信息
        findurl = os.popen("adb shell pm path com.pingan.wetalk").read()
        # 截取包路径
        print findurl.split(':')[1].strip()
        # os.popen("adb uninstall com.pingan.wetalk")
    else:
        print "Install first"
        os.popen("adb install"+" "+path)
        os.popen("adb shell input keyevent 3")
        path = os.popen("adb shell pm path com.pingan.wetalk").read()
        print path.split(':')[1].strip()
        # print "Then uninstall"
        # os.popen("adb uninstall com.pingan.wetalk")
    print "Install successed."


# 第二节课2:实现自动获取当前连接电脑的设备ID
def get_deviceID():
    print "start get deviceid"
    deviceID = os.popen("adb devices").read()
    print "The attached deviceid is "+deviceID.split()[4]


# 第二节课3:实现如果存在则启动app,按home键,杀进程,如果不存在先安装再启动
def launch():
    print "start lanuch..."
    packages = os.popen("adb shell pm list packages ").read()
    path = "/Users/huajie/Desktop/txt_test.apk"
    if packages.find("com.pingan.wetalk") != -1:
        print "Just launch it."
        # 启动app
        os.popen("adb shell am start -n com.pingan.wetalk/com.pingan.wetalk.module.splash.activity.SplashActivity")
        # android应用启动很慢,等一等才能看到效果
        time.sleep(30)
        os.popen("adb shell input keyevent 3")
        os.popen("adb shell am force-stop com.pingan.wetalk")
    else:
        print "Install first"
        os.popen("adb install"+" "+path)
        time.sleep(5)
        # 安装后需要点击确定安装(使用坐标，如下坐标基于三星S6 Edge)
        os.popen("adb shell input tap 720 2480")
        print "Then launch it."
        # 启动app
        os.popen("adb shell am start -n com.pingan.wetalk/com.pingan.wetalk.module.splash.activity.SplashActivity")
        # os.popen("adb shell input keyevent 3")
        # os.popen("adb shell am force-stop com.pingan.wetalk")


# 第三节课:使用adb完成一张截图并保存
def screenshot():
    print "Start get the screenshot..."
    os.popen("adb shell /system/bin/screencap -p /sdcard/screenshot.png")


# 第四节课:通过aapt解析指定apk包，并且得到该apk包的包名与LauchActivity名，并输出
def get_apkinfo():
    print "start get the apkinfo by aapt"
    path = "/Users/huajie/Desktop/txt_test.apk"
    # 列出包所有信息并按包名过滤
    apkinfo_name = os.popen("aapt dump badging "+path+"|grep package").read()
    # 按'分割字符串取第二即可
    package_name = apkinfo_name.split("'")[1]
    # 列出包所有信息并按启动activity过滤
    apkinfo_activity = os.popen("aapt dump badging "+path+"|grep launchable-activity").read()
    # 按'分割字符串取第二即可
    launch_activity = apkinfo_activity.split("'")[1]
    print "The package name is "+package_name
    print "The lanuch activity is "+launch_activity


# 第五次课:当你的电脑连接着两台设备时，自动获取第一台设备，使用adb进行安装卸载操作
def get_first_device():
    print "start install apk to the appointed device"
    path = "/Users/huajie/Desktop/txt_test.apk"
    # 列出所有的device
    devices = os.popen("adb devices").read()
    # 根据空格分割取出第一个device id
    first_device_id = devices.split()[4]
    # 指定id设备上进行安装和卸载
    os.popen("adb -s "+first_device_id+" install "+path)
    time.sleep(5)
    # 进行device的操作也需要-s指定设备
    os.popen("adb -s "+first_device_id+" shell input keyevent 3")
    time.sleep(3)
    # 卸载
    os.popen("adb -s "+first_device_id+" uninstall com.pingan.wetalk")
    time.sleep(3)


# 第6次课:封装一个点击某个坐标的方法
def tap_point():
    print "Start tap setting"
    # 调用公共方法点击"设置"按钮的坐标
    common.click_by_adb(700, 2200)


if __name__ == '__main__':
    tap_point()
    print "Finished"

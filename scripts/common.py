# encoding: utf-8

# 第六次课：点击手机屏幕的某个位置
import os


def click_by_adb(x, y):
    print "Start tap anypoint point"
    cmd = "adb shell input tap"+" "+str(x)+" "+str(y)
    os.popen(cmd)

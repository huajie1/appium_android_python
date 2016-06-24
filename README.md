# appium_android_python
appium_android_python 学习

一、uiautomator的学习  

1.首先要新建一个Java工程，将android.jar和uiautomator.jar添加到依赖->写脚本->最后按照如下操作来做  
2.uiautomator生成build.xml文件：cd 第1步新建的项目目录执行如下命令  
```android create uitest-project -n uiautomator -t 3 -p <你的项目路径>```  
3.生成之后修改build.xml:  
``` <project name="uiautomator" default="build">```  
4.使用ant 生成jar(当然你肯定要先配置ant环境):  
```ant -buildfile <你的项目路径>```  
5.push jar 包到手机(放到tmp目录下执行时不用指定包的路径了)  
```adb push <生成的你的jar包路径>  /data/local/tmp/```  
6.执行测试用例  
```adb shell uiautomator runtest <你的jar包名.jar> -c <包名.类名#方法名>```  

二、python的学习

代码注释已经写的很清楚了，如要参考，请修改apk包路径、包名即可  

三、脚本编写  

简单实现启动、登录，如要参考，app/路径下放本人的测试apk，修改设备信息、包名、启动activity即可  


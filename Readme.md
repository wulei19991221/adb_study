### uiautomator2自动化
1. 初始化,给安卓安装所需软件

> 开启adb,开发者模式(手机)
>> cmd输入adb devices查看是否连接成功
>>> 连接成功,cmd输入python -m uiautomator2 init 
>> 等待安装成功

2.安装浏览器调试工具weditor
```
pip install weditor
python -m weditor
```

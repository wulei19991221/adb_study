# !/usr/bin/python3
# --coding:utf-8--
# @Author:ACHIEVE_DREAM
# @Time: 2020年05月30日14时
# @File: demo1.py
import uiautomator2 as ui
import time
start = time.time()
d = ui.connect('fff2a99c')
d(text="淘宝特价版").click()
print(f'successful time : {time.time() - start:.2f}')
time.sleep(2)
d.click(0.851, 0.041)
time.sleep(2)
d.click(0.9, 0.963)
time.sleep(1)
d.click(0.293, 0.524)
time.sleep(6)
SX = 0.165 * 1000
EX = 0.883 * 1000
SY = 0.275 * 1000
EY = 0.720 * 1000
LENGTH = 0.06 * 1000
for i in range(int(SX), int(EX), int(LENGTH)):
    for j in range(int(SY), int(EY), int(LENGTH)):
        d.click(i / 1000, j / 1000)
        time.sleep(0.05)

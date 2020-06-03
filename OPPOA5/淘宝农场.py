# !/usr/bin/python3
# --coding:utf-8--
# @Author:ACHIEVE_DREAM
# @Time: 2020年05月30日15时
# @File: 淘宝农场.py
import uiautomator2 as u2
import time
from print_color import *
from threading import Thread, Lock


class TaobaoFarm:
    def __init__(self):
        Thread(target=self.print_loading_style, args=(5, '开始')).start()
        self.d = u2.connect('fff2a99c')
        # self.d = u2.connect('192.168.1.24')
        print_c(fgreen, '连接成功')
        # self.goto_farm()

    # 从淘宝软件桌面进去
    def goto_farm(self):
        self.d(text="淘宝特价版").click()
        time.sleep(2)
        # 跳过广告
        self.click(0.851, 0.041)
        time.sleep(2)
        # 进入我的
        self.click(0.9, 0.963)
        time.sleep(2)
        # 农场
        self.click(0.293, 0.524)
        time.sleep(10)

    # 扫描农场区域
    def scan_screen(self):
        SX = 0.165 * 1000
        EX = 0.883 * 1000
        SY = 0.275 * 1000
        EY = 0.720 * 1000
        LENGTH = 0.06 * 1000
        for i in range(int(SX), int(EX), int(LENGTH)):
            for j in range(int(SY), int(EY), int(LENGTH)):
                self.click(i / 1000, j / 1000)
                time.sleep(0.01)

    # 重写点击事件
    def click(self, x, y):
        self.d.click(x, y)
        print_c(fyellow, f'点击: {x * 1000}, {y * 1000}')

    # 偷阳光
    def steal_people(self):
        for _ in range(30):
            self.click(0.716, 0.768)  # 偷阳光按钮
            time.sleep(5)  # 加载5秒
            self.click(0.572, 0.288)  # 获取阳光
            self.click(0.073, 0.06)  # 左上角返回
            time.sleep(1)

    # 领取产物,每一分钟一次
    def current_farm_click(self):
        print_c(fyellow, '开始收取')
        while True:
            self.click(0.312, 0.599)
            self.click(0.514, 0.649)
            self.click(0.512, 0.557)
            self.click(0.296, 0.496)
            self.print_loading_style(60 * 10, '开始收取作物')

    @staticmethod
    def print_loading_style(need_time: int, msgs: str):
        for _ in range(need_time, 0, -1):
            print_c(fgreen, '', end=f'\r{_}秒后{msgs}')
            time.sleep(1)

    # 领阳光
    def receive_sun(self):
        print_c(fyellow, '开始领取阳光')
        self.click(0.903, 0.757)  # 领取阳光
        for _ in range(3):
            time.sleep(0.05)
            self.click(0.849, 0.817)  # 进入页面
            self.print_loading_style(17, '结束浏览')
            self.click(0.076, 0.059)  # 返回农场
            time.sleep(0.5)
            self.click(0.92, 0.707)  # 关闭领取页面
            print_c(fred, f'还剩余{3 - _}次免费机会')
            self.print_loading_style(60*10, '开始浏览')
        self.scan_screen()

    def run(self):
        # self.steal_people()
        # x, y = eval(input_c(fblue, '输入点击位置: '))
        # self.click(x, y)
        # 领取产物
        t = Thread(target=self.current_farm_click)
        t.start()
        time.sleep(0.5)
        t1 = Thread(target=self.receive_sun)
        t1.start()
        time.sleep(21)
        t2 = Thread(target=self.steal_people)
        t2.start()


if __name__ == '__main__':
    taobao = TaobaoFarm()
    taobao.run()

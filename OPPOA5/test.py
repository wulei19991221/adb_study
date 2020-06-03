# !/usr/bin/python3
# --coding:utf-8--
# @Author:ACHIEVE_DREAM
# @Time: 2020年05月30日19时
# @File: test.py
from threading import Thread, Lock
from time import sleep

def test():
    lock.acquire()
    # for i in range(100):
    #     print(i, 'test1')
    #     sleep(1)
    for i in range(100):
        i += 1
        print(i, 'test1')
        sleep(1)
    lock.release()


def test2():
    lock.acquire()
    a = 1
    # for i in range(100):
    #     print(i, 'test2')
    #     sleep(1)
    # print('locked')
    for i in range(100):
        i += 1
        print(i, 'test2')
        sleep(1)
    lock.release()


lock = Lock()
if __name__ == '__main__':
    Thread(target=test).start()
    Thread(target=test2).start()

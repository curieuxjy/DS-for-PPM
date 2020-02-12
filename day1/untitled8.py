# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:27:18 2020

@author: LG
"""

from threading import Timer
from time import sleep

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

def displayWhenCalled1():
  print('Timer event occured. timer1')
def displayWhenCalled2():
  print('                     timer2')

# 시간 간격은 처리되는 시간 제외하고 1초가 지난 후 실행된다.
# 타이머에 대한 핸들 rt, 해당 클래스를 부르기 위한 이름
rt1 = RepeatedTimer(1, displayWhenCalled1)
rt2 = RepeatedTimer(2, displayWhenCalled2)
#쓰레딩이 뒤에서 돌고 있음
try:
  sleep(10)
finally:
  rt1.stop()
  rt2.stop()

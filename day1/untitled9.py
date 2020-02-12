# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:41:15 2020

@author: LG
"""

from threading import Timer
from time import sleep
from urllib.request import urlopen
import bs4

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
        
def getCurrentStockPrice():
#  idx_stock = '004170'
  naver_index = 'https://finance.naver.com/item/main.nhn?code=' + idx_stock
  
  source = urlopen(naver_index).read()
  source = bs4.BeautifulSoup(source, 'lxml')
  
  
  curPrice1 = source.find_all('em', class_='no_up')[0]
#  print(curPrice1)
  curPrice2 = curPrice1.find_all('span')[0].text
#  print(curPrice2)
  curPrice3 = int(curPrice2.replace(',', ''))
  print(curPrice3)
  ###########csv 파일 저장
  tmpTime = dt.datatime.now()
  curTime = tmpTime.strftime('%Y-%m-%d %H:%M:%S')
  #########3 값이 변하는 것처럼 만들기 위해서
  if True:
    rndCurPrice = 
  #########
  return curPrice3

print('Start')
idx_stock = '004170'
rt1 = RepeatedTimer(1, getCurrentStockPrice, idx_stock)
#rt1 = RepeatedTimer(1, getCurrentStockPrice)

try:
  sleep(10)
finally:
  rt1.stop()

  

  
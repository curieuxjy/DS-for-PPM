# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:45:26 2020

@author: LG
"""
# 주가 가져오기
# db를 위한 import
import sqlite3
# timer를 위한 import
from threading import Timer
from time import sleep
# stockprice 가져오기 위한 import
from urllib.request import urlopen
import bs4
import datetime as dt

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

#
#dbpath = 'curStockPrice.db'
##연결
#conn = sqlite3.connect(dbpath)
##커서
#cur = conn.cursor()

def getCurStockPrice(idx_stock):
  
#  cur = conn.cursor()
  #------------------------StockId--------------------------
  
  StockId = idx_stock
  naver_index = 'https://finance.naver.com/item/main.nhn?code=' + StockId

  #---------------------------------------------------
  
  source = urlopen(naver_index).read()
  source = bs4.BeautifulSoup(source, 'lxml')
  
  #-----------------------curPrice--------------------------
  curPrice = source.find_all('em', class_='no_up')[0]
  curPrice = curPrice.find_all('span')[0].text
  curPrice = int(curPrice.replace(',', ''))
#  print(curPrice)
  #------------------------curDate---------------------------
  tmpDate = dt.datetime.now()
  curDate = tmpDate.strftime('%Y-%m-%d')
  curTime = tmpDate.strftime('%H:%M:%S')
  #------------------------------------------------------
  insertDB(StockId, curDate, curTime, curPrice)


def insertDB(StockId, curDate, curTime, curPrice):
  dbpath = 'curStockPrice.db'
  #연결
  conn = sqlite3.connect(dbpath)
  #커서
  cur = conn.cursor()
  
  strSQL = 'INSERT INTO curStockPrice (StockId, curDate, curTime, curPrice)\nVALUES(?, ?, ?, ?)'
  
  try:
    # cur vs conn?
    cur.execute(strSQL, (StockId, curDate, curTime, curPrice))
    print("good")
    conn.commit()
  except:
    conn.rollback()
  conn.close()
  
  

print('Start')

idx_stock = '004170'
rt1 = RepeatedTimer(5, getCurStockPrice, idx_stock )

try:
  sleep(100)
finally:
  rt1.stop()
  
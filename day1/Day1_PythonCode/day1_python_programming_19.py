
# [실습 7] 주가 조회하기 - Timer

from threading import Timer
from time import sleep
import bs4
from urllib.request import urlopen
import datetime as dt
import random as rnd
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Timer 출처
# https://stackoverflow.com/questions/3393612/run-certain-code-every-n-seconds
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
        
def getCurrentStockPrice(idx_stock):
    naver_index = 'https://finance.naver.com/item/sise.nhn?code=' + idx_stock
    source = urlopen(naver_index).read()
    source = bs4.BeautifulSoup(source, 'lxml')
    
    curPrice1 = source.find_all('em', class_='no_up')[0]
    curPrice2 = curPrice1.find_all('span')[0].text
#    curPrice = curPrice2.replace(',','')
    curPrice = float(curPrice2.replace(',',''))
    
    tmpTime = dt.datetime.now()
    curTime = tmpTime.strftime('%Y-%m-%d %H:%M:%S')
    
    if True:
        rndCurPrice = curPrice
    else:
        rndCurPrice = math.ceil(curPrice * rnd.gauss(1, 0.1))
    
    print(idx_stock, ',', curTime, ',', rndCurPrice)
    
    historicalData[curTime] = str(rndCurPrice)

    return historicalData

print('Starting...')
idx_stock = '004170'

historicalData = dict()
rt = RepeatedTimer(1, getCurrentStockPrice, idx_stock)
try:
    sleep(5) 
finally:
    rt.stop()

tmpData4Plot = {'신세계': historicalData}
dfHistoricalData = pd.DataFrame(tmpData4Plot)
dfHistoricalData.to_csv('004170_Stock_Price.csv')           # csv 저장



#
#x = np.zeros([int(dfHistoricalData.shape[0]),1])
#x = dfHistoricalData.values
#
#plt.figure(1, figsize = (10, 5))
#plt.plot(dfHistoricalData, color='b', linestyle='-', marker='o', markersize=10)
#plt.legend(loc=0)
#plt.grid(True, color='0.7', linestyle=':', linewidth=1)
#plt.xlabel('Time')
#plt.ylabel('Price')
#plt.title('Stock Price')
#plt.show()
#
#
#

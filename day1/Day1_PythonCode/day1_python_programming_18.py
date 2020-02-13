# [실습 7] 주가 조회하기 - Timer
from threading import Timer
from time import sleep
import bs4
from urllib.request import urlopen
import datetime as dt

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
#    print(curPrice1)
    
    curPrice2 = curPrice1.find_all('span')[0].text
#    print(curPrice2)

#    curPrice = int(curPrice2.replace(',',''))
    curPrice = curPrice2.replace(',','')
    
    tmpTime = dt.datetime.now()
#    curTime = str(tmpTime.year) + '-' + str(tmpTime.month) + '-' + str(tmpTime.day) \
#              + ' ' \
#              + str(tmpTime.hour) + ':' + str(tmpTime.minute) + ':' + str(tmpTime.second)         
    curTime = tmpTime.strftime('%Y-%m-%d %H:%M:%S')
        
    print(idx_stock, ',', curTime, ',', curPrice)

    return curPrice

print('Starting...')
idx_stock = '004170'
rt = RepeatedTimer(1, getCurrentStockPrice, idx_stock)
try:
    sleep(10) 
finally:
    rt.stop()
    
    
    
    
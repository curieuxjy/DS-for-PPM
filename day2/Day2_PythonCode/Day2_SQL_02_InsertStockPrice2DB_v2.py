from threading import Timer
from time import sleep
import bs4
from urllib.request import urlopen
import datetime as dt
import sqlite3


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

def insert2DB(stockID, curTime, curPrice):
    dbpath = 'chinook.db'
    conn = sqlite3.connect(dbpath)
    
    strSQL = 'INSERT INTO curStockPrice (StockID, curDate, curPrice) '
    strSQL = strSQL + 'Values (' 
    strSQL = strSQL + '"' + stockID + '"'
    strSQL = strSQL + ', ' 
    strSQL = strSQL + '"' + curTime + '"'
    strSQL = strSQL + ', '
    strSQL = strSQL + ' ' + str(int(curPrice)) + ' )'
    
    try:
        conn.execute(strSQL)
        conn.commit()
    except:
        conn.rollback()
        
    conn.close()
    
    return

def getCurrentStockPrice(idx_stock):
    naver_index = 'https://finance.naver.com/item/sise.nhn?code=' + idx_stock
    source = urlopen(naver_index).read()
    source = bs4.BeautifulSoup(source, 'lxml')
    
    curPrice1 = source.find_all('em', class_='no_up')[0]
    curPrice2 = curPrice1.find_all('span')[0].text
    curPrice = float(curPrice2.replace(',',''))
    
    tmpTime = dt.datetime.now()
    curTime = tmpTime.strftime('%Y-%m-%d %H:%M:%S')
  
    insert2DB(idx_stock, curTime, curPrice)
    
    return 


#---------------------------------------------------------------
#dbpath = 'chinook.db'
#conn = sqlite3.connect(dbpath)

print('Starting...')
idx_stock = '004170'

rt = RepeatedTimer(1, getCurrentStockPrice, idx_stock)
try:
    sleep(10) 
finally:
    rt.stop()
    
    
    

# [실습 5] 주가 조회하기

import bs4
from urllib.request import urlopen
 
idx_stock = '004170'
naver_index = 'https://finance.naver.com/item/sise.nhn?code=' + idx_stock
 
source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')
#print(source.prettify())
 
#curPrice1 = source.find_all('em', class_='no_up')
curPrice1 = source.find_all('em', class_='no_up')[0]
print(curPrice1)

curPrice2 = curPrice1.find_all('span')[0].text
print(curPrice2)
#
curPrice3 = int(curPrice2.replace(',',''))
print(curPrice3)



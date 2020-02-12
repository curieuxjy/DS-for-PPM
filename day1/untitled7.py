# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:11:25 2020

@author: LG
"""
from urllib.request import urlopen
import bs4

idx_stock = '004170'
naver_index = 'https://finance.naver.com/item/main.nhn?code=' + idx_stock

source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, 'lxml')


curPrice1 = source.find_all('em', class_='no_up')[0]
curPrice2 = curPrice1.find_all('span')[0].text
curPrice3 = int(curPrice2.replace(',', ''))

print(curPrice3)

#
#price = source.find_all('td', class_='num')[0]
#print(price)
#
#tmp_strong = source.find_all('strong', class_='tah p11')[0]
#tmp_value = tmp_strong.text
#print(tmp_value)
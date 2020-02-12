# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:19:48 2020

@author: LG
"""

import urllib.request as req
import urllib.parse
from bs4 import BeautifulSoup


def mission():
  local_name = input("어느 지역의 날씨를 알고 싶습니까?")
  local_dict = {'전국':'108', '서울/경기도':'109', '강원도':'105', '충청북도':'131',\
                '충청남도':'133', '전라북도':'146', '전라남도':'156', '경상북도':'143',\
                '경상남도':'159', '제주특별자치도':'184'}
  local_num = local_dict[local_name]
  print(local_num)
  
  API = 'https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp'
  loc_id = {'stnId':local_num} #stnId 바꾸면 안됨!!
  print(loc_id)
  
  params = urllib.parse.urlencode(loc_id)
  print(params)
  url = API + "?" + params
  print(url)
  
  source = req.urlopen(url)
  source = BeautifulSoup(source, "html.parser")
#  print(source)
#  print(source.prettify())
  
  tmp_title = source.find('title').string
  print(tmp_title)
  
  tmp_province = source.find('province').string
  print(tmp_province)
  
  
  tmp_date = source.find_all('tmef')[1].text
  tmp_weather = source.find_all('wf')[1].text
  
  return tmp_date, tmp_weather, tmp_province

date, weather, province = mission()


'''
API = 'https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp'
loc_id = {'stn_id':local_num} #서울 경기도 지역코드 109

params = urllib.parse.urlencode(loc_id)
url = API + "?" + params
print(url)

source = req.urlopen(url)
source = BeautifulSoup(source, "html.parser")
print(source)
print(source.prettify())

#########################
tmp_title = source.find('title').string
print(tmp_title)

tmp_province = source.find('province').string
print(tmp_province)

# tmef의 갯수로 크기 짐작
lst_data = source.find_all('tmef')

for i in range(len(lst_data)):
  tmp_date = source.find_all('tmef')[i].text
  tmp_weather = source.find_all('wf')[i].text
  
  print(tmp_province, ', ', tmp_date, ', ', tmp_weather)
'''
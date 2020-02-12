# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:05:30 2020

@author: LG
"""

import urllib.request
import urllib.parse

API = 'https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp'
loc_id = {'stn_id':'109'} #서울 경기도 지역코드 109

params = urllib.parse.urlencode(loc_id)
url = API + "?" + params
print(url)

rtn_data = urllib.request.urlopen(url).read()
print(rtn_data)
#읽을 수 없음

rtn_text = rtn_data.decode("utf-8")
print(rtn_text) #tag로 이루어져 있음 -> beautifulsoup으로!
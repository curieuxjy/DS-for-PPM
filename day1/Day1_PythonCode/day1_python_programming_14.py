# Scraping & Crawling

# [실습 3] 기상청 싸이트에서 기상정보 가져오기

import urllib.request
import urllib.parse

API = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

locID = {'stnId':'109'}     # 서울/경기도 109

params = urllib.parse.urlencode(locID)
url = API + "?" + params
print(url)

rtnData = urllib.request.urlopen(url).read()
print(rtnData)


rtnText = rtnData.decode("utf-8")
print(rtnText)

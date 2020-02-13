# Scraping & Crawling

# [실습 4] 기상청 싸이트에서 기상정보 가져오기

import urllib.request as req
import urllib.parse
from bs4 import BeautifulSoup

def getWeatherForecast(locID):
    API = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
    
    #locID = {'stnId':'109'}     # 서울/경기도 109
    # 전국 108, 서울/경기도 109, 강원도 105, 충청북도 131, 충청남도 133
    # 전라북도 146, 전라남도 156, 경상북도 143, 경상남도 159, 제주특별자치도 184
    
    params = urllib.parse.urlencode(locID)
    url = API + "?" + params
#    print(url)
    
    source = req.urlopen(url)
    source = BeautifulSoup(source, "html.parser")
    
    tmpTitle = source.find('title').string
    tmpProvince = source.find('province').string
    lstDate = source.find_all('tmef')
    
    tmpDate = source.find_all('tmef')[1].text
    tmpWeather = source.find_all('wf')[1].text
#    print(tmpProvince, ', ', tmpDate, ', ', tmpWeather)

    return tmpProvince, tmpDate, tmpWeather

strLoc = input('지역을 입력하세요: ')

if strLoc == '서울':
    locID = {'stnId':'109'}
elif strLoc == '제주':
    locID = {'stnId':'184'}
else:
    locID = {'stnId':'000'}
    print('해당지역 없음')

tmpProvince, tmpDate, tmpWeather = getWeatherForecast(locID)
print(tmpProvince, ', ', tmpDate, ', ', tmpWeather)



    
    
#for i in range(0, len(lstDate)):
#    tmpDate = source.find_all('tmef')[i].text
#    tmpWeather = source.find_all('wf')[i].text
#    
#    print(tmpProvince, ', ', tmpDate, ', ', tmpWeather)




#source = BeautifulSoup(source, "html.parser")
##print(source)
##print(source.prettify())
#
#tmpTitle = source.find('title').string
##print(tmpTitle)
#
#tmpProvince = source.find('province').string
##print(tmpProvince)
#
#lstDate = source.find_all('tmef')
##print(len(lstDate))
#
#for i in range(0, len(lstDate)):
#    tmpDate = source.find_all('tmef')[i].text
#    tmpWeather = source.find_all('wf')[i].text
#    
#    print(tmpProvince, ', ', tmpDate, ', ', tmpWeather)
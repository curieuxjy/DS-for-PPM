# Scraping & Crawling

# 예제: 홍익대학교 홈페이지에서 학교 로고 읽어와 저장하기

import urllib.request

strUrl = 'http://www.hongik.ac.kr/front/images/local/header_logo1.png'
strFileName = 'hongik_logo.png'

## Case #1
#urllib.request.urlretrieve(strUrl, strFileName)
#print('저장 완료')

# Case #2
#rtn = urllib.request.urlretrieve(strUrl, strFileName)
#print(rtn)
#print(type(rtn))
#print('저장 완료')
#    
# Case #3 -  Error Handling (try/except)
try:
    rtn = urllib.request.urlretrieve(strUrl, strFileName)
    print(rtn)
    print('저장 완료')
except:
    print('Not found')

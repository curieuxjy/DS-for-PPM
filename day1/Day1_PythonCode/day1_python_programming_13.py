# Scraping & Crawling

# 예제: 홍익대학교 홈페이지에서 학교 로고 읽어와 저장하기

import urllib.request

strUrl = 'http://www.hongik.ac.kr/front/images/local/header_logo.png'
strFileName = 'hongik_logo222.png'

# 해당 이미지를 읽고 메모리에 로딩
imgLogo = urllib.request.urlopen(strUrl).read()
#print(imgLogo)

# 파일로 저장
with open(strFileName, mode='wb') as f:
    f.write(imgLogo)
    print('파일 저장 완료')
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:48:34 2020

@author: LG
"""

import urllib.request
str_url = 'http://www.hongik.ac.kr/front/images/local/header_logo.png'
str_filename = 'hongik_logo.png'

#왜 변수 저장이 안되어 있지? -> 의미를 알 수 없기 때문에 variable 창에 뜨지 않음
img_logo = urllib.request.urlopen(str_url).read()

# line by line 저장
# wb: binary file write

#with open(str_filename, mode = 'wb') as f:
#  f.write(img_logo)
#  print('saved')
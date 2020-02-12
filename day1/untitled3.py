# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:41:53 2020

@author: LG
"""
import urllib.request
str_url = 'http://www.hongik.ac.kr/front/images/local/header_logo.png'
str_filename = 'hongik_logo.png'

# case 1
urllib.request.urlretrieve(str_url, str_filename)
print('saved')

# case 2 return 확인
rtn = urllib.request.urlretrieve(str_url, str_filename)
print(rtn)
print(type(rtn))

#case3 error
#str_url = 'http://www.hongik.ac.kr/font/images/local/header_logo.png'
try: 
  rtn = urllib.request.urlretrieve(str_url, str_filename)
  print(rtn)
  print('saved')
except:
  print('not found')
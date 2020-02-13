# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 09:08:35 2020

@author: LG
"""

import sqlite3

dbpath = 'chinook.db'
#연결
conn = sqlite3.connect(dbpath)

#커서
cur = conn.cursor()
# SQL 문
strSQL = 'SELECT * FROM employees'
#실행
cur.execute(strSQL)
item_list = cur.fetchall()
# fetch 가져오다
for it in item_list:
  print(it)

print(item_list[0]) 
print(item_list[0][1])
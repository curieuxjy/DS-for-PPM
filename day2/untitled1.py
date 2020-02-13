# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:28:35 2020

@author: LG
"""

import sqlite3

dbpath = 'chinook.db'
#연결
conn = sqlite3.connect(dbpath)

#커서
cur = conn.cursor()
# SQL 문
strSQL = 'INSERT INTO employees (EmployeeId, LastName, FirstName)'
strSQL = strSQL + '\nVALUES(' + str(1234) + ', ' + '"Lee", ' +'"Jungyeon")'
print(strSQL)

#실행
cur.execute(strSQL)
# tranjection을 임시로 해보고 오류가 나면 rollback
conn.commit()
# auto commit이 안됨
# 데이터를 영구적으로 넣어줌
conn.close()

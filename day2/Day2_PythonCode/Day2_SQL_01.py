import sqlite3

dbpath = 'chinook.db'
conn = sqlite3.connect(dbpath)

cur = conn.cursor()

#strSQL = 'SELECT * FROM employees'

#strSQL = 'INSERT INTO employees (EmployeeId, LastName, FirstName) '
#strSQL = strSQL + 'Values (' + str(1234)
#strSQL = strSQL + ', ' 
#strSQL = strSQL + '"OH"'
#strSQL = strSQL + ', '
#strSQL = strSQL + '"YOUKEUN"'
#strSQL = strSQL + ')'
strSQL = 'INSERT INTO employees (EmployeeId, LastName, FirstName) '
strSQL = strSQL + 'Values (' + str(1234)
strSQL = strSQL + ', ' 
strSQL = strSQL + '"OH"'
strSQL = strSQL + ', '
strSQL = strSQL + '"YOUKEUN"'
strSQL = strSQL + ')'

print(strSQL)

cur.execute(strSQL)
conn.commit()

#item_list = cur.fetchall()
#
#for it in item_list:
#    print(it)
#    
#print(item_list[0][1])



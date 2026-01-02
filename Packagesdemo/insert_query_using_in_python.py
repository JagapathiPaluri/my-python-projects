import sqlite3
conn = sqlite3.connect(r"D:\Python Software\SQLlite_Database_is_here\testdb.sqlite3")
cur = conn.cursor()
qry = """INSERT INTO EMPLOYEE(FIRST_NAME,
   LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Rambabu', 'Paluri', 31, 'M', 300000)"""

try:
   cur.execute(qry)
   conn.commit()
   print ('Record inserted successfully')
except Exception as e:
   conn.rollback()
   print ('error in INSERT operation')
   print (e)
conn.close()
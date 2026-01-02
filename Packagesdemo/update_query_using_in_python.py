import sqlite3
conn=sqlite3.connect(r'D:\Python Software\SQLlite_Database_is_here\testdb.sqlite3')
cur=conn.cursor()
qry="UPDATE EMPLOYEE SET INCOME = INCOME * 10 WHERE INCOME=? and first_name=?"

try:
   # Execute the SQL command
   cur.execute(qry, (50000, "Makrand"))
   # Fetch all the rows in a list of lists.
   conn.commit()
   print ("Records updated")
except Exception as e:
   print ("Error: unable to update data")
conn.close()
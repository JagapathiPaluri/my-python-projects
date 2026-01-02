import sqlite3
conn=sqlite3.connect(r'D:\Python Software\SQLlite_Database_is_here\testdb.sqlite3')
cur=conn.cursor()
qry="SELECT FIRST_NAME, LAST_NAME, AGE, SEX, INCOME FROM EMPLOYEE"

try:
   # Execute the SQL command
   cur.execute(qry)
   # Fetch all the rows in a list of lists.
   results = cur.fetchall()
   for row in results:
      first_name = row[0]
      last_name = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # Now print fetched result
      print ("first_name={}, last_name={}, age={}, sex={}, income={}".format(first_name, last_name, age, sex, income ))
except Exception as e:
   print (e)
   print ("Error: unable to fecth data")

conn.close()
import sqlite3
conn=sqlite3.connect(r'D:\Python Software\SQLlite_Database_is_here\testdb.sqlite3')
cur=conn.cursor()
qry="SELECT * FROM EMPLOYEE"

try:
   # Execute the SQL command
   cur.execute(qry)
   # Fetch all the rows in a list of lists.
   results = cur.fetchone()
   first_name = results[1]
   last_name = results[2]
   age = results[3]
   sex = results[4]
   income = results[5]
      
# Now print fetched result
   print ("first_name={}, last_name={}, age={}, sex={}, income={}".format(first_name, last_name, age, sex, income ))
except Exception as e:
   print (e)
   print ("Error: unable to fecth data")

conn.close()
import mysql.connector

conn=mysql.connector.connect(host='localhost',username='root',password='password@098',database='qsardb')

my_cursor=conn.cursor()

conn.commit()
conn.close()

print("connection sucessfully created")

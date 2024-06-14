import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='')
print(mydb)

# create database
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='')
mycursor=mydb.cursor()
mycursor.execute('CREATE DATABASE mca')

# create table
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mca')
mycursor=mydb.cursor()
mycursor.execute('create table stud(id int, name varchar(100))')

# insert records
import mysql.connector
try:
	mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mca')
	insert_rec='insert into stud(id,name) values(%s,%s)'
	myrecords=[(1,'sunday'),(2,'monday'),(3,'tuesday')]
	cursor=mydb.cursor()
	cursor.executemany(insert_rec,myrecords)
	mydb.commit()
	print('Inserted Successfully')
except mysql.connector.Error as error:
	print('Fail to insert')
finally:
	if mydb.is_connected():
		cursor.close()
		mydb.close()
		print('Mysql Connection is closed Successfully...')

# to display
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mca')
mycursor=mydb.cursor()
mycursor.execute('select *from stud')
result=mycursor.fetchall()
for i in result:
	print(i)

# update records
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mca')
mycursor=mydb.cursor()
mycursor.execute('update stud set name="saturday" where id=3')
mydb.commit()
mydb.close()

# delete records
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mca')
mycursor=mydb.cursor()
mycursor.execute('delete from stud where id=3')
mydb.commit()
mydb.close()
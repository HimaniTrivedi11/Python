# create connection
import sqlite3
cnt=sqlite3.connect('mydb.exam')

# create table
cnt.execute('CREATE TABLE stud_mca (id integer ,name varchar,city varchar)')
print('Table created..........')

# insert data
cnt.execute("""INSERT INTO stud_mca values(1,'monday','rjk'),(2,'tuesday','mumbai'),(3,'wednesday','pune')""")
print("Recorded Successfully")
cnt.commit()

# retrieve data from the databse
cursor=cnt.execute('SELECT *FROM stud_mca')
for i in cursor:
	print(i)

# update data
upd_sql="""UPDATE stud_mca set name='friday' where id=1 """
cnt.execute(upd_sql)
cursor=cnt.execute('SELECT *FROM stud_mca')
for i in cursor:
	print(i)

# delete data
del_sql="""DELETE FROM stud_mca WHERE id=2"""
cnt.execute(del_sql)
cursor=cnt.execute('SELECT *FROM stud_mca')
for i in cursor:
	print(i)


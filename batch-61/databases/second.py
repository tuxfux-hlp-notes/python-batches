#!/usr/bin/python
import MySQLdb as mdb
conn = mdb.connect('localhost','user61','user61','batch61')  # connection
# connection datails : server,username,password,database
cursor = conn.cursor()  # Curson is for running queiries on your database.
cursor.execute('create table students (name varchar(10),gender varchar(6))') # executes a query for us.
'''
mysql> show tables;
Empty set (0.00 sec)
'''
conn.close()
'''
After running the program
mysql> show tables;
+-------------------+
| Tables_in_batch61 |
+-------------------+
| students          |
+-------------------+
1 row in set (0.00 sec)

mysql> desc students;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| name   | varchar(10) | YES  |     | NULL    |       |
| gender | varchar(6)  | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
2 rows in set (0.01 sec)
'''

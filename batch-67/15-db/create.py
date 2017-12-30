#!/usr/bin/python
import MySQLdb as mdb
conn = mdb.connect('localhost','user67','user67','batch67')
#conn = mdb.connect('db servername','username','password','database')
cur = conn.cursor()
cur.execute('create table student (name varchar(10),gender varchar(6))')
conn.close()

'''
mysql> show tables;
+-------------------+
| Tables_in_batch67 |
+-------------------+
| student           |
+-------------------+
1 row in set (0.00 sec)

mysql> desc student;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| name   | varchar(10) | YES  |     | NULL    |       |
| gender | varchar(6)  | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
2 rows in set (0.00 sec)

mysql> select * from student;
Empty set (0.00 sec)

mysql> 
'''
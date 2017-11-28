#!/usr/bin/python
import MySQLdb as mdb
con = mdb.connect('localhost','user66','user66','batch66')
cur = con.cursor()
cur.execute('create table student (name varchar(10),gender varchar(6))')
con.close()

'''
mysql> select database();
+------------+
| database() |
+------------+
| batch66    |
+------------+
1 row in set (0.00 sec)

mysql> show tables;
+-------------------+
| Tables_in_batch66 |
+-------------------+
| student           |
+-------------------+
1 row in set (0.01 sec)

mysql> desc student;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| name   | varchar(10) | YES  |     | NULL    |       |
| gender | varchar(6)  | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
2 rows in set (0.00 sec)

mysql> 

'''
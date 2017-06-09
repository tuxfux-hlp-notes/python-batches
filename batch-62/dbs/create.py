#!/usr/bin/python
import MySQLdb as mdb
conn = mdb.connect('localhost','user62','user62','batch62')
cur = conn.cursor()
cur.execute("create table students (name varchar(20),gender varchar(6))")
conn.close()


'''
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| batch62            |
+--------------------+
2 rows in set (0.00 sec)

mysql> use batch62;
Database changed
mysql> show tables;
+-------------------+
| Tables_in_batch62 |
+-------------------+
| students          |
+-------------------+
1 row in set (0.00 sec)

mysql> desc students;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| name   | varchar(20) | YES  |     | NULL    |       |
| gender | varchar(6)  | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
2 rows in set (0.00 sec)

'''

#!/usr/bin/python
import MySQLdb as mq
con = mq.connect('localhost','user58','user58','batch58')
cur = con.cursor()
cur.execute('create table student(name varchar(25),gender varchar(6))')
con.close()



'''
mysql> help create table;

mysql> use batch58;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> select database();
+------------+
| database() |
+------------+
| batch58    |
+------------+
1 row in set (0.00 sec)

mysql> show tables;
+-------------------+
| Tables_in_batch58 |
+-------------------+
| student           |
+-------------------+
1 row in set (0.00 sec)

mysql> desc student;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| name   | varchar(25) | YES  |     | NULL    |       |
| gender | varchar(6)  | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
2 rows in set (0.00 sec)

mysql> select * from student;
Empty set (0.00 sec)

mysql> 

'''

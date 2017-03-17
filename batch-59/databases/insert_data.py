#!/usr/bin/python
import MySQLdb as mq
con = mq.connect('localhost','user58','user58','batch58')
cur = con.cursor()
name = raw_input("please enter your name?")
gender = raw_input("please enter your gender?")
cur.executemany("insert into student(name,gender) values (%s,%s)" , [(name,gender)])
con.commit() # transation
con.close()

'''
mysql> show create table student;
+---------+---------------------------------------------------------------------------------------------------------------------------------------+
| Table   | Create Table                                                                                                                          |
+---------+---------------------------------------------------------------------------------------------------------------------------------------+
| student | CREATE TABLE `student` (
  `name` varchar(25) DEFAULT NULL,
  `gender` varchar(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+---------+---------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)

mysql> show engines;
+--------------------+---------+----------------------------------------------------------------+--------------+------+------------+
| Engine             | Support | Comment                                                        | Transactions | XA   | Savepoints |
+--------------------+---------+----------------------------------------------------------------+--------------+------+------------+
| MyISAM             | YES     | MyISAM storage engine                                          | NO           | NO   | NO         |
| CSV                | YES     | CSV storage engine                                             | NO           | NO   | NO         |
| MRG_MYISAM         | YES     | Collection of identical MyISAM tables                          | NO           | NO   | NO         |
| BLACKHOLE          | YES     | /dev/null storage engine (anything you write to it disappears) | NO           | NO   | NO         |
| MEMORY             | YES     | Hash based, stored in memory, useful for temporary tables      | NO           | NO   | NO         |
| PERFORMANCE_SCHEMA | YES     | Performance Schema                                             | NO           | NO   | NO         |
| ARCHIVE            | YES     | Archive storage engine                                         | NO           | NO   | NO         |
| InnoDB             | DEFAULT | Supports transactions, row-level locking, and foreign keys     | YES          | YES  | YES        |
| FEDERATED          | NO      | Federated MySQL storage engine                                 | NULL         | NULL | NULL       |
+--------------------+---------+----------------------------------------------------------------+--------------+------+------------+
9 rows in set (0.00 sec)

mysql> select * from student;
+-------+--------+
| name  | gender |
+-------+--------+
| rajni | f      |
+-------+--------+
1 row in set (0.00 sec)

mysql> 

'''
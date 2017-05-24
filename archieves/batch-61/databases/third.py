#!/usr/bin/python
import MySQLdb as mdb
name = raw_input("please enter your name:")
gender = raw_input("please enter your gender:")
conn = mdb.connect('localhost','user61','user61','batch61')  # connection
# connection datails : server,username,password,database
cursor = conn.cursor()  # Curson is for running queiries on your database.
cursor.executemany('insert into students (name,gender) values (%s,%s)',[(name,gender)]) # executes a query for us.
conn.commit()
conn.close()

'''
mysql> select * from students;
+-------+--------+
| name  | gender |
+-------+--------+
| kumar | m      |
+-------+--------+
1 row in set (0.00 sec)

mysql> show create table students;
+----------+----------------------------------------------------------------------------------------------------------------------------------------+
| Table    | Create Table                                                                                                                           |
+----------+----------------------------------------------------------------------------------------------------------------------------------------+
| students | CREATE TABLE `students` (
  `name` varchar(10) DEFAULT NULL,
  `gender` varchar(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+----------+----------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)

mysql> show engines;
+--------------------+---------+----------------------------------------------------------------+--------------+------+------------+
| Engine             | Support | Comment                                                        | Transactions | XA   | Savepoints |
+--------------------+---------+----------------------------------------------------------------+--------------+------+------------+
| MyISAM             | YES     | MyISAM storage engine                                          | NO           | NO   | NO         |
| MRG_MYISAM         | YES     | Collection of identical MyISAM tables                          | NO           | NO   | NO         |
| PERFORMANCE_SCHEMA | YES     | Performance Schema                                             | NO           | NO   | NO         |
| BLACKHOLE          | YES     | /dev/null storage engine (anything you write to it disappears) | NO           | NO   | NO         |
| InnoDB             | DEFAULT | Supports transactions, row-level locking, and foreign keys     | YES          | YES  | YES        |
| CSV                | YES     | CSV storage engine                                             | NO           | NO   | NO         |
| ARCHIVE            | YES     | Archive storage engine                                         | NO           | NO   | NO         |
| MEMORY             | YES     | Hash based, stored in memory, useful for temporary tables      | NO           | NO   | NO         |
| FEDERATED          | NO      | Federated MySQL storage engine                                 | NULL         | NULL | NULL       |
+--------------------+---------+----------------------------------------------------------------+--------------+------+------------+
9 rows in set (0.00 sec)
'''

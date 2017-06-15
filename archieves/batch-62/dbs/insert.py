#!/usr/bin/python
import MySQLdb as mdb
name = raw_input("please enter your name:")
gender = raw_input("please enter your gender:")
conn = mdb.connect('localhost','user62','user62','batch62')
cur = conn.cursor()
cur.executemany("insert into students (name,gender) values (%s,%s)",[(name,gender)])
conn.commit()
conn.close()
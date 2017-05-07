#!/usr/bin/python
import MySQLdb as mdb
name = raw_input("please enter your name:")
gender = raw_input("please enter your gender:")
con = mdb.connect('localhost','user57','user57','batch57')
# con - handle - variable name
# mdb.connect(server,username,password,database)
cur = con.cursor()
cur.executemany("insert into student(name,gender) values (%s,%s)",[(name,gender)])
con.commit()
con.close()
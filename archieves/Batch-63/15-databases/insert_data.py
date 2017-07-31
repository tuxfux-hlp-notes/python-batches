#!/usr/bin/python
import MySQLdb as mdb
#con = mdb.connect('servername','username','password','databasename')
name = raw_input("please enter your name:")
gender = raw_input("please enter your gender:")
con = mdb.connect('localhost','user63','user63','batch63')
cur = con.cursor()
cur.executemany("insert into student (name,gender) values (%s,%s)",[(name,gender)])
con.commit()  # this is a must as our table student is using a innodb engine
con.close()
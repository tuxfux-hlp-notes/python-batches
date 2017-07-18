#!/usr/bin/python
import MySQLdb as mdb
#con = mdb.connect('servername','username','password','databasename')
con = mdb.connect('localhost','user63','user63','batch63')
cur = con.cursor()
cur.execute("create table student (name varchar(20),gender varchar(6))")
con.close()
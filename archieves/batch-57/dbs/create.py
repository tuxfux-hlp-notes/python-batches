#!/usr/bin/python
import MySQLdb as mdb
con = mdb.connect('localhost','user57','user57','batch57')
# con - handle - variable name
# mdb.connect(server,username,password,database)
cur = con.cursor()
cur.execute("create table student (name varchar(10),gender varchar(6))")
con.close()
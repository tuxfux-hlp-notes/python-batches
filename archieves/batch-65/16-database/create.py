#!/usr/bin/python

import MySQLdb as mdb
con = mdb.connect('localhost','user65','user65','batch65')
cur = con.cursor()
cur.execute("create table student (name varchar(10),gender varchar(6))")
con.close()

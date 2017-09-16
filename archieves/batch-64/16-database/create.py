#!/usr/bin/python

import MySQLdb as mdb
con = mdb.connect('localhost','user64','user64','batch64')
cur = con.cursor()
cur.execute("create table student (name varchar(10),gender varchar(6))")
con.close()

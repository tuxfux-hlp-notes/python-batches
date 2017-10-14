#!/usr/bin/python

import MySQLdb as mdb
con = mdb.connect('localhost','user65','user65','batch65')
# con = mdb.connect(servername,username,password,database)
cur = con.cursor() # A cursor to connect to a database - con(represents our database.)
cur.execute("select version()")
output = cur.fetchone()
print output[0].split('-')[0]
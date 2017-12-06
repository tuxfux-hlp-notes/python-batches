#!/usr/bin/python
#!/usr/bin/python
import MySQLdb as mdb
name = raw_input("please enter your name:")
gender = raw_input("please enter your gender:")
con = mdb.connect('localhost','user66','user66','batch66')
cur = con.cursor()
cur.executemany("insert into student(name,gender) values (%s,%s)",[(name,gender)])
con.commit()
con.close()

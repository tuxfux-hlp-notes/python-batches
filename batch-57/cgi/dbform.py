#!/usr/bin/env python 
print "Content-type: text/html" 
print 
print "<html>"
print "<body>"
print "<form action='action.py' method='post'>"
print "Name: <input type='text' name='name' /><br>"
print "Gender:<input type='text' name='gender'/><br>"
print "<input type='submit' />"
print "</form>"
print "</body>"
print "</html>"

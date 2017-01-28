#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter?
# man date
# streamHandler is a file like object but not a file - ex: console

# Challenges
# basicConfig only support , SteamHandler and FileHandler.
# name of the logger is always root. 
# This is only for dev testing - team is 5 members.


 
import logging as l

l.basicConfig(filename="my_log.txt",filemode="a",level=l.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%c')


l.debug("this is an debugging message")
l.info("this is an informational message")
l.warning("this is a warning message")
l.error("This is an error message")
l.critical("This is an critical message")
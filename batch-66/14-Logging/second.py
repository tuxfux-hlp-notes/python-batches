#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter?
# man date.

import logging as l

l.basicConfig(filename='my_file.log',filemode='a',level=l.DEBUG,
			  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%c')

# modes
# r -> read mode -> you can only the read the file.
# w -> write mode -> you can write into a file.
# * if the file is having some content,truncates your file to zero.
# * if the file doesnt exits, we get a new file created and content into it.
# a -> append mode -> you can append into the file.

l.debug("This is an debug message.")
l.info("This is an information message.")
l.warning("This is an warning message.")
l.error("This is an error message.")
l.critical("This is an critical message")
#!/usr/bin/python
import re
reg = re.compile("kh.*?on",re.I)
with open('/var/log/syslog') as f:
	for my_string in f:
		m = reg.search(my_string)
		print my_string[:m.start()] + my_string[m.end():]



'''
my_string="Sep  1 19:00:07 khyaathipython gnome-session[2110]: gnome-session-binary[2110]: GLib-GIO-CRITICAL: g_dbus_connection_call_internal: assertion 'object_path != NULL && g_variant_is_object_path (object_path)' failed"
import re
reg = re.compile("kh.*?on",re.I)
print reg.search(my_string).group()
m = reg.search(my_string)
print m
print dir(m)
print m.start(),m.end()
print my_string
print my_string[:m.start()] + my_string[m.end():]
'''
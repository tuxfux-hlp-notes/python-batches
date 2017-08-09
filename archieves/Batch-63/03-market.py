#!/usr/bin/python
# pass : block filler - it doesnt do anything.
# Logical operators - and/or
# Number of logical comparisions - exceeding 2 - re

print "welcome to the market"
food_type = raw_input("please enter your foodtype - fish/chicken/meat/veg:")

if food_type == 'fish':
	print "welcome to the fish market"
	fish_type = raw_input("please enter your fish type - elish/solomon/rohu/fillets : ")
	if fish_type == 'elish' or fish_type == 'Elish':
		print "we have your fish type - {}".format(fish_type)
		print "how much quantity of fish type - {} you need".format(fish_type)
	elif fish_type == 'solomon':
		print "we have your fish type - {}".format(fish_type)
		print "how much quantity of fish type - {} you need".format(fish_type)
	elif fish_type == 'rohu':
		print "we have your fish type - {}".format(fish_type)
		print "how much quantity of fish type - {} you need".format(fish_type)
	else:
		print "we dont have your fish type - {}".format(fish_type)
		print "How about chicken/meat/veg"
elif food_type == 'meat':
	pass
elif food_type == 'chicken':
	pass
elif food_type == 'veg':
	pass
else:
	pass
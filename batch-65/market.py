#!/usr/bin/python
# pass - block filler
# and/or logical operators

print "welcome to the market"
food_type = raw_input("please enter  your food type - fish/meat/chicken/veg:")

if food_type == 'fish':
	print "welcome to the fish market"
	fish_type = raw_input("what is the fish type you need - pamplet/rohu/tofu/fillets:")
	if fish_type == 'rohu' or fish_type == 'ROHU':
		print "we have your fish type - {}".format(fish_type)
		print "what quantity of fish you need"
	elif fish_type == 'tofu':
		print "we have your fish type - {}".format(fish_type)
		print "what quantity of fish you need"
	elif fish_type == 'solomon':
		print "we have your fish type - {}".format(fish_type)
		print "what quantity of fish you need"
	else:
		print "we DONT have your fish type - {}".format(fish_type)
		print "how about chicken/meat/veg"		
elif food_type == 'meat':
	pass
elif food_type == 'chicken':
	pass
elif food_type == 'veg':
	pass
else:
	pass
#!/usr/bin/python
# pass: a block filler
# logical operators : and/or

print "welcome to the market"
food_type = raw_input("please enter your food type: veg/chicken/meat/fish - ")

if food_type == 'chicken':
	pass
elif food_type == 'meat':
	pass
elif food_type == 'fish':
	print "welcome to the fish market."
	fish_type = raw_input("please enter yoru fish - solomon/tofu/rohu/fillets:")
	if fish_type == 'rohu':
		print "we have your {}".format(fish_type)
		print "how much quantity of fish {} you need".format(fish_type)
	elif fish_type == 'solomon':
		print "we have your {}".format(fish_type)
		print "how much quantity of fish {} you need".format(fish_type)
	elif fish_type == 'tofu' or fish_type == 'TOFU':
		print "we have your {}".format(fish_type)
		print "how much quantity of fish {} you need".format(fish_type)
	else:
		print "we DONT have your {}".format(fish_type)
		print "how about chicken/meat/veg"
elif food_type == 'veg':
	pass
else:
	pass
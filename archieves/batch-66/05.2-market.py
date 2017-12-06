#!/usr/bin/python
#  pass: block filler - it does nothing.
# logical operators - and/or

print "welcome to the market"
food_type = raw_input("please enter the item- meat/fish/chicken/veg: ")

if food_type == 'meat':
    pass
elif food_type == 'fish':
    print "welcome to the fish market."
    fish_type = raw_input("please enter your fish type - solomon/rohu/tofu/fillets:")
    if fish_type == 'solomon':
        print "we have your fish {}".format(fish_type)
        print "how much quantity of fish {} you need".format(fish_type)
    elif fish_type == 'tofu' or fish_type == 'TOFU':
        print "we have your fish {}".format(fish_type)
        print "how much quantity of fish {} you need".format(fish_type)  
    elif fish_type == 'rohu':
        print "we have your fish {}".format(fish_type)
        print "how much quantity of fish {} you need".format(fish_type)  
    else:
        print "we DONT have your fish {}".format(fish_type)
        print "HOW about chicken/meat/veg."   
elif food_type == 'chicken':
    pass
elif food_type == 'veg':
    pass
else:
    pass


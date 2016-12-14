#!/usr/bin/python
# logical operations - and/or
print "welcome to the market"
food_type = raw_input("please enter your food type - chicken/meat/fish/veg :")

if food_type == 'fish':
    print "welcome to the fish market"
    fish_type = raw_input("please enter the fish type - tuna/pamplet/solomon/rohu:")
    if fish_type == 'tuna' or fish_type == 'TUNA':
        print "we have your fish type {}".format(fish_type)
        print "how much quantity of fish {} you need".format(fish_type)
    elif fish_type == 'rohu':
        print "we have your fish type {}".format(fish_type)
        print "how much quantity of fish {} you need".format(fish_type)
    elif fish_type == 'solomon':
        print "we have your fish type {}".format(fish_type)
        print "how much quantity of fish {} you need".format(fish_type)
    else:
        print "we don't have your fish type {}".format(fish_type)
        print "how about chicken/meat/veg"        
elif food_type == 'meat':
    pass
elif food_type == 'chicken':
    pass
elif food_type == 'veg':
    pass
    

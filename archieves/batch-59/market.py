#!/usr/bin/python
# pass: block filler,pass does nothing.
# Logical operators: and/or

print "welcome to the market"
food_type = raw_input("please enter your food type? - chicken/meat/fish/veg:")

if food_type == 'chicken':
    pass
elif food_type == 'meat':
    pass
elif food_type == 'fish':
    print "welcome to the fish market"
    fish_type = raw_input("please enter your fish type? - solomon/rohu/tuna/fillets: ")
    if fish_type == 'solomon':
        print "we have your fish type {}".format(fish_type)
        print "how much quantity of {} you need".format(fish_type)
    elif fish_type == 'rohu' or fish_type == 'ROHU':
        print "we have your fish type {}".format(fish_type)
        print "how much quantity of {} you need".format(fish_type)
    elif fish_type == 'tuna':
        print "we have your fish type {}".format(fish_type)
        print "how much quantity of {} you need".format(fish_type)
    else:
        print "we don't have your fish type {}".format(fish_type)
        print "how about chicken/meat/veg"    
elif food_type == 'veg':
    pass
else:
    pass
    
 

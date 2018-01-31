#!/usr/bin/python
# pass : block filler .. it has nothing to do.
# logical operators : and/or

print "welcome to the market"

food_type = raw_input("please enter your food type - chicken/meat/veg/fish:")

if food_type == 'fish':
    print "welcome to the fish market"
    fish_type = raw_input("please enter your fish type: solomon/rohu/tofu/fillets - ")
    if fish_type == 'solomon':
        print "we have your fish type {}".format(fish_type)
        print "how much quantity of  fish  you need"
    elif fish_type == 'rohu':
        print "we have your fish type {}".format(fish_type)
        print "how much quantity of  fish  you need"    
    elif fish_type == 'tofu' or fish_type == 'TOFU':
        print "we have your fish type {}".format(fish_type)
        print "how much quantity of  fish  you need"
    else:
        print "we DONT have your fish type {}".format(fish_type)
        print "how about chicken/meat/veg"  
elif food_type == 'meat':
    pass
elif food_type == 'veg':
    pass
elif food_type == 'chicken':
    pass
else:
    pass
#!/usr/bin/python
# pass : block holder
# logical operators: or/and
print "welcome to the market"
food_type = raw_input("what is your food type - fish/meat/chicken/veg :")

if food_type == 'fish':
    print "welcome to the fish market"
    fish_type = raw_input("what fish you need - cod/tuna/solomon/rohu:")
    if fish_type == 'cod' or fish_type == 'COD':
        print "we have you fish type {} available".format(fish_type)
        print "how much quantity of fish type {} you need".format(fish_type)
    elif fish_type == 'tuna':
        print "we have you fish type {} available".format(fish_type)
        print "how much quantity of fish type {} you need".format(fish_type)
    elif fish_type == 'rohu':
        print "we have you fish type {} available".format(fish_type)
        print "how much quantity of fish type {} you need".format(fish_type)
    else:
        print "we don't have your fish type {} available".format(fish_type)
        print "how about chicken/meat/veg"
elif food_type == 'meat':
    pass
elif food_type == 'chicken':
    pass
elif food_type == 'veg':
    pass
else:
    pass


    
    

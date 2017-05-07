#!/usr/bin/python
# pass : I have nothing for you. Please move on. Block filler.
# and/or

print "welcome to the market"
food_type = raw_input("please enter your food type - meat/fish/chicken/veg:")


if food_type == 'meat':
    pass
elif food_type == 'fish':
    print "welcome to the fish market"
    fish_type = raw_input("please enter fish type - tuna/rohu/solomon/fillets:")
    if fish_type == 'tuna':
        print "your fish type {} is available".format(fish_type)
        print "how much quantity of {} you need".format(fish_type)
    elif fish_type == 'rohu':
        print "your fish type {} is available".format(fish_type)
        print "how much quantity of {} you need".format(fish_type)
    elif fish_type == 'solomon':
        print "your fish type {} is available".format(fish_type)
        print "how much quantity of {} you need".format(fish_type)
    else:
        print "your fish type {} is not available".format(fish_type)
        print "We also have chicken,meat and veg"  
elif food_type == 'chicken':
    pass
elif food_type == 'veg':
    pass

#!/usr/bin/python
# pass: its a block filler or in short - i have nothing to do.
# logical operations : or/and

print "welcome to the market"
food_type = raw_input("what is your food type - fish/mutton/chicken/veg: ")

if food_type == 'fish':
    print "welcome to the fish market"
    fish_type = raw_input("please enter the fish type - tuna/pomplet/solomon/rohu :")
    if fish_type == 'tuna':
        print "we have your fish type {}".format(fish_type)
        print "how much quantity of fish you need {}".format(fish_type)
    elif fish_type == 'rohu' or fish_type == "ROHU":
        print "we have your fish type {}".format(fish_type)
        print "how much quantity of fish you need {}".format(fish_type)
    elif fish_type == 'solomon':
        print "we have your fish type {}".format(fish_type)
        print "how much quantity of fish you need {}".format(fish_type)
    else:
        print "we dont have your fish type {}".format(fish_type)
        print "how about chicken/mutton/veg"    
elif food_type == 'mutton':
    pass
elif food_type == 'chicken':
    pass
elif food_type == 'veg':
    pass
else:
    pass
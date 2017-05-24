#!/usr/bin/python
# pass - block filler doesnot do anything.
# logical operators: and/or

print "welcome to the market"
food_type = raw_input("please enter your food type - fish/meat/chicken/veg:")

if food_type == 'fish':
    print "welcome to the fish market"
    fish_type = raw_input("what fish your need - solomon/rohu/fillets/tuna:")
    if fish_type == 'solomon' or fish_type == 'SOLOMON':
        print "we have your fish type {}".format(fish_type)
        print "how much quantity of {} you need".format(fish_type)
    elif fish_type == 'rohu':
        print "we have your fish type {}".format(fish_type)
        print "how much quantity of {} you need".format(fish_type)
    elif fish_type == 'fillets':
        print "we have your fish type {}".format(fish_type)
        print "how much quantity of {} you need".format(fish_type)
    else:
        print "we dont have your fish type {}".format(fish_type)
        print "how about meat/chicken/veg"
elif food_type == 'meat':
    pass
elif food_type == 'chicken':
    pass
elif food_type == 'veg':
    pass
    
    

  
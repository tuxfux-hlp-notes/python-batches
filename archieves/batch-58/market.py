#!/usr/bin/python
# pass - a block filler or means nothing.
# Logical operators: or/and

print "welcome to the market"
food_type = raw_input("what do you want to buy - meat/chicken/fish/veg:")

if food_type == 'meat':
    pass
elif food_type == 'chicken':
    pass
elif food_type == 'fish':
    print "welcome to the fish market"
    fish_type = raw_input("what fish you need - solomon/tuna/fillets/rohu :")
    if fish_type == 'solomon':
        print "we have your fish {}".format(fish_type)
        print "how much quantity of {} you need".format(fish_type)
    elif fish_type == 'tuna' or fish_type == 'TUNA':
        print "we have your fish {}".format(fish_type)
        print "how much quantity of {} you need".format(fish_type)
    elif fish_type == 'fillets':
        print "we have your fish {}".format(fish_type)
        print "how much quantity of {} you need".format(fish_type)
    else:
        print "sorry!! you fish type is not available"
        print "how about chicken/meat/veg"        
elif food_type == 'veg':
    pass
else:
    pass
    
    
    
    
    

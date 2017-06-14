#!/usr/bin/python
# pass : block filler
# PEP8 - https://www.python.org/dev/peps/pep-0008/#code-lay-out
# https://www.youtube.com/watch?v=wf-BqAjZb8M
# logical operators - and/or

print "welcome to the market"
food_type = raw_input("what food type you need - veg/fish/meat/chicken :")

if food_type == 'fish':
    print "welcome to the fish market"
    fish_type = raw_input("what fish you need - solomon/tuna/fillets/rohu :")
    if fish_type == 'solomon':
        print "your fish type {} is available".format(fish_type)
        print "how much quantity of fish {} you need".format(fish_type)
    elif fish_type == 'tuna' or fish_type == 'TUNA':
        print "your fish type {} is available".format(fish_type)
        print "how much quantity of fish {} you need".format(fish_type)
    elif fish_type == 'fillets':
        print "your fish type {} is available".format(fish_type)
        print "how much quantity of fish {} you need".format(fish_type)
    else:
        print "your fish type {} is not available".format(fish_type)
        print "how about chicken/meat/veg"
elif food_type == 'meat':
    pass
elif food_type == 'chicken':
    pass
elif food_type == 'veg':
    pass
else:
    pass
    

#!/usr/bin/python


# Defining a class in pytohn.
#class account(object):
#class account:

class account:      # <type 'classobj'>/class
	balance = 0     # class schema variable.
	def deposit(self,amount):
		self.balance = self.balance + amount
		return self.balance
	def withdraw(self,amount):
		self.balance = self.balance - amount
		return self.balance
	def final(self):
		print "my initial balance is {}".format(self.balance)


print type(account)   # <type 'classobj'>/class
print type(account()) # <type 'instance'>/object



# sandeep
sandeep = account()   # i created an object - sandeep for class account.
print dir(sandeep)    # ['__doc__', '__module__', 'balance', 'deposit']
print type(sandeep)   # <type 'instance'>/object
# print help(sandeep.deposit) # method

print "Initial balance of sandeep {}".format(sandeep.balance)
sandeep.deposit(1000)
sandeep.final()



# Sunil

sunil = account()
print "Initial balance of sunil {}".format(sunil.balance)
sunil.deposit(5000)
sunil.final()

# santosh
santosh = account
print dir(santosh)
print santosh.balance
santosh.balance=100000
print santosh.balance
print santosh.final()


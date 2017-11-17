#!/usr/bin/python
# method - constructor

# blueprint
# class Account(object):
# class Account:
class Account:
	def __init__(self):  # Function gets initiated automatically.
		self.balance = 0
	def bal(self):  # self denotes the instance itself
		return "my balance is {}".format(self.balance)

# sri
sri = Account
print dir(sri)


ashok = Account()
print dir(ashok)
print ashok.bal()

kumar = Account()
kumar.balance = 1000
print kumar.bal()





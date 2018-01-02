class Account():
	def __init__(self):   # constructor
		self.balance = 0
	def my_withdraw(self,amount):
		self.amount = amount
		self.balance = self.balance - self.amount
	def my_deposit(self,amount):
		self.amount = amount
		self.balance = self.balance + self.amount
	def my_balance(self):
		return "my balance is {}".format(self.balance)

class MinBalAccount(Account):
	def __init__(self):
		Account.__init__(self)
	def my_withdraw(self,amount):
		if self.balance - amount < 1000:
			print "buddy!! time to call your daddy!!!"
		else:
			Account.my_withdraw(self,amount)


##
sri = Account()
sri.my_deposit(10000)
sri.my_withdraw(7000)
sri.my_withdraw(7000) 
print sri.my_balance()

## balu
balu = MinBalAccount()
balu.my_deposit(10000)
balu.my_withdraw(7000)
balu.my_withdraw(7000)
balu.my_withdraw(2000)
print balu.my_balance()



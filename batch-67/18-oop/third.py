class Account():
	def __init__(self):
		self.balance = 0
	def my_withdraw(self):
		self.balance = self.balance - 300
	def my_deposit(self):
		self.balance = self.balance + 1000
	def my_balance(self):
		return "my balance is {}".format(self.balance)


##
sri = Account()
sri.my_deposit() # 1000
sri.my_deposit() # 2000
sri.my_withdraw() # 1700
print sri.my_balance()



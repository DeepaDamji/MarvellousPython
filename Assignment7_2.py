class BankAccount:
	roi=10.5;

	def __init__(self, name, amount):
		self.name=name;
		self.amount=int(amount);

	def deposite(self):
		print("\nEnter Amount to Deposite in Account : ");
		self.depositeAmount=int(input());
		self.amount=self.amount+self.depositeAmount;

	def withdraw(self):
		print("\nEnter Amount to Withdraw from Account : ");
		self.withdrawAmount=int(input());
		self.amount=self.amount-self.withdrawAmount;

	def calculateInterest(self):
		self.interest=(self.amount * 2 * BankAccount.roi) / 100;
		print("\nInterest on Rs.",self.amount,"For 2 Years : ",self.interest);

	def display(self):
		print("\nName : ",self.name);
		print("Amount : ",self.amount);

def main():
	print("\n\n*** OOP (Encapsulation) Program to Display Bank Details ***\n");
	name=input("\nEnter Name :");
	amount=int(input("Enter Amount : "));
	b=BankAccount(name, amount);
	b.deposite();
	b.display();
	b.withdraw();
	b.display();
	b.calculateInterest();	

if __name__ == "__main__":
	main();




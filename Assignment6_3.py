class Arithmetic:
	def __init__(self):
		value1=0.0;
		value2=0.0;

	def accept(self):
		value1=int(input("Enter 1st Value : "));
		self.value1=value1;
		value2=int(input("Enter 2nd Value : "));
		self.value2=value2;

	def addition(self):
		return self.value1+self.value2;

	def subtraction(self):
		return self.value1-self.value2;

	def multiplication(self):
		return self.value1*self.value2;

	def division(self):
		return self.value1/self.value2;

def main():
	a=Arithmetic();
	print("\n\n*** OOP (Encapsulation) Program to Perform Arithmetic Operations ***\n\n")

	a.accept();
	print("\nAddition : ",a.addition());
	print("Subtraction : ",a.subtraction());
	print("Multiplication : ",a.multiplication());
	print("Division : ",a.division());

if __name__ == "__main__":
	main();



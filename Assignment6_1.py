class Demo : 
	value=10;

	def __init__(self, n1, n2) :
		self.no1=n1;
		self.no2=n2;

	def fun(self) :
		print("Displaying Values from Fun : ",self.no1, " ", self.no2);

	def gun(self) :
		print("Displaying Values from Gun : ",self.no1, " ", self.no2);

def main() :
	print("OOP Program Demonstrating Encapsulation")
	obj1=Demo(11, 21);
	obj2=Demo(51, 101);

	obj1.fun();
	obj2.fun();
	obj1.gun();
	obj2.gun();

if __name__ == "__main__" :
	main();

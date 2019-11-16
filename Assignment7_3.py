class Numbers:
	def __init__(self, value):
		self.value=value;

	def chkPrime(self):
		i=2;
		count=0;
		newValue=self.value;
		while i < newValue :
			res=newValue%i;
			if res == 0 :
				count=count+1;
				break;
			else:
				pass;
			i=i+1;
			
		if count == 1 :
			return False;
		else :
			return True;

	def chkPerfect(self):
		i=1;
		count=0;
		global divisor;
		divisor=list();
		newValue=self.value;

		while i < newValue :
			res=newValue%i;
			if res == 0 :
				count=count+1;
				divisor.append(i);
			else:
				pass
			i=i+1;

		if count >= 1 :
			if sum(divisor)==newValue :
				return True;
			else :
				return False;
		else :
			return False;

	def factors(self):
		print("Factors : ",divisor);
			
	def sumFactors(self):
		return sum(divisor);

def main():
	print("\n\n*** OOP (Encapsulation) Program for Different Operations on Number ***\n\n")
	value=int(input("Enter a Number : "));
	n=Numbers(value);

	print("\nPrime Number : ",n.chkPrime());
	print("Perfect Number : ",n.chkPerfect());
	n.factors();

if __name__ == "__main__":
	main();



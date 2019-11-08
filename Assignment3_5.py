import MarvellousNum;

def ListPrime() :
	print("Enter Number of Elemets : ");
	size = int(input());
	arr=list()
	
	print("Enter Elements : ");
	for i in range(0, size, 1) :
		no=int(input());
		arr.append(no);
	
	MarvellousNum.ChkPrime(arr);

print("\n\n****Program to Find Addition of Prime Numbers in List****\n\n");  
ListPrime();
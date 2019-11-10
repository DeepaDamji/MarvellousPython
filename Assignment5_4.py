print("\n\n****Recursive Program for Summation of Digits in Number****\n\n");
add=0;
def addNumber(n) :
	res=int(n%10);
	
	if res==0 :
		return;
	else :
		global add;
		add=add+res;
		return(addNumber(int(n/10)));
	
print("Enter Number : ");
no=int(input());

addNumber(no);
print("Summation of All Digits : ", add);


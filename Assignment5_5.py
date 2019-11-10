print("\n\n****Recursive Program to calculate factorial****\n\n");

res=1;
def factorial(no) :
	if no==1 :
		return;
	else :
		global res;
		res=res*no;
		return factorial(no-1);

print("Enter Number : ");
no=int(input());
factorial(no);
print("Factorial : ", res);
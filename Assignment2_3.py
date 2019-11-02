def factorial(no):
	num=int(no);
	i=1;
	res=1;

	while i <= num :
		res=res*i;
		i=i+1;
	
	print("Factorial of ",num," : ",res);

print("\n\n****Factorial Program****\n\n");
print("Enter a Number ");
no=input();
factorial(no);
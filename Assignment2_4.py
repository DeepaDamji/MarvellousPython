def addition(no):
	num=int(no);
	i=1;
	add=0;

	while i < num :
		rem=num%i;
		
		if rem == 0 :
			add=add+i;
		else:
			pass;
		i=i+1;
	
	print(add);

print("\n\n****Program to Display Addition of Factors****\n\n");
print("Enter a number ");
num=input();

addition(num);

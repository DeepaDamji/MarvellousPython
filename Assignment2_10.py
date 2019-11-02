def addNumber(no) :

	num=int(no);
	add=0;

	while num != 0 :
		res=num%10;
		res=int(res);
		add=add+res;
		num=num/10;
		num=int(num);

	print(add);

print("\n\n****Program to Add Digits in Given Number****\n\n");
print("Enter a Number ");
no=input();
addNumber(no);

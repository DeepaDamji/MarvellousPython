def numberOfDigits(no) : 
	num=int(no);
	c=0;
	res=0;

	while  num >= 1 :
		res=num%10;
		res=int(res);
		c=c+1;
		num=num/10;
		num=int(num);
			
	print(c);

print("\n\n****Program to Find Number of Digits in Given Number****\n\n");
print("Enter a Number ");
no=input();
numberOfDigits(no);

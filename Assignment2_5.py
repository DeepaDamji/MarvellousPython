def prime(no):
	num=int(no);
	i=2;
	count=0;

	while i < num :
		res=num%i;
				
		if res == 0 :
			count=count+1;
			break;
		else:
			pass;
		i=i+1;
		
	if count == 1 :
		print("Number is Not Prime");
	else :
		print("Number is Prime");

print("\n\n****Program to Find Prime Number****\n\n");
print("Enter a Number ");
no=input();
prime(no);


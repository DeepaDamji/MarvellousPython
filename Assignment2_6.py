def display(no) : 
	
	num=int(no);
	row = 1;
	count=num;

	while row <= num :
		col=count;
		
		while col >= 1 :
			print("*", end=" ");
			col=col-1;
		
		print("\n");
		row=row+1;
		count=count-1;

print("\n\n****Program to Display Pattern****\n\n");	
print("Enter a Number ");
no=input();
display(no);


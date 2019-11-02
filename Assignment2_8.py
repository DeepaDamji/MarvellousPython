def display(no) :
	num=int(no);

	row=1;
	col=1;
	
	while row <= num : 
		count=1;
		while count <= col :
			print(count, end="  ");
			count=count+1;
		col=col+1;
		print("\n");
		row=row+1;

print("\n\n****Program to Display Pattern****\n\n");
print("Enter a Number");
no=input();
display(no);


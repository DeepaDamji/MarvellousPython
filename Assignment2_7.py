def display(no) :
	num=int(no);

	row=1;
	count=num;

	while row <= num : 
		col=1;
		while col <= num :
			print(col, end="  ");
			col=col+1;
		print("\n");
		row=row+1;

print("Enter a Number");
no=input();
display(no);


def displaypattern(no):
	row=0;
	num=int(no);
	while row < num :
		col=0;
		while col < num :
			print("*",end=" ");
			col=col+1;
		row=row+1;
		print("\n");

print("\n\n****Program to Display Pattern****\n\n");
print("Enter a Number ");
num=input();

displaypattern(num); 
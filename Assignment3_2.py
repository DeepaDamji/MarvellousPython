print("\n\n****Program to Find Maximum Number****\n\n");

print("Enter Number of Elements : ");
size=int(input());

print("Enter Elements : ");

arr=list();

for i in range(0, size, 1) :
	no=int(input());
	arr.append(no);

print("Maximum Number is : ", max(arr));


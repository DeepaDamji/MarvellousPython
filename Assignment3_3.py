print("\n\n****Program to Find Minimum Value****\n\n");

print("Enter Number of Elements : ");

size=int(input());
arr=list();

for i in range(0, size, 1) :
	no=int(input());
	arr.append(no);

print("Mininmum Value : ", min(arr));
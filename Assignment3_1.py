print("\n\n****Program to Add all Numbers on List****\n\n");

size=int(input("Enter Number of Elements : "));
arr=list();

print("Enter Elements : ");

for i in range(0, size, 1) :
	no=input();
	arr.append(int(no));
	
print(sum(arr));

	
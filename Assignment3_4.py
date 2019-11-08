print("\n\n****Program to Find Frequency of Number in List****\n\n");

print("Enter Number of Elements : ");

size=int(input());
arr=list();

print("Enter Elements : ");

for i in range(0, size, 1) :
	no=int(input());
	arr.append(no);

print("Enter a Number : ");
no=int(input());

print(arr);

cnt=arr.count(no);
print("Frequency : ", cnt)
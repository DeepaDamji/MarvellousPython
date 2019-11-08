from functools import *;

def prime(no) :
	i=2;
	count=0;
	while i<no :
		res=no%i;
		if res == 0 :
			count=count+1;
			break;
		else : 
			pass
		i=i+1;
	if count == 1 :
		return False;
	else :
		return True;

def multiply(no) :
	return no*2;

def maxNumber(no1, no2) :
	return max(no1, no2);

print("\n\n****Program Using FMR to Calculate Sum of Even Numebrs****\n\n");

print("Enter Number of Elements : ");
size=int(input());
arr=list();

print("Enter Elements : ");
for i in range(0, size, 1) :
	no=int(input());
	arr.append(no);

print("Original List : ", arr);

brr=list(filter(prime, arr));
print("Prime Nmbers : ", brr);
crr=list(map(multiply, brr));
print("Multiplied Numbers : ", crr);
ans=reduce(maxNumber, crr);
print("Maximum Number : ", ans);
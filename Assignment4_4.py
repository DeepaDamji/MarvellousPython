from functools import *;

def Chkeven(no) :
	if no%2 == 0 :
		return True;
	
def square(no) :
	return no*no;

def addition(no1, no2) :
	return no1+no2;

print("\n\n****Program Using FMR to Calculate Sum of Even Numebrs****\n\n");

print("Enter Number of Elements : ");
size=int(input());
arr=list();

print("Enter Elements : ");
for i in range(0, size, 1) :
	no=int(input());
	arr.append(no);

print("Original List : ", arr);
brr=list(filter(Chkeven, arr));
print("Even Numbers : ", brr);
crr=list(map(square, brr));
print("Square Roots : ", crr);
ans=reduce(addition, crr);
print("Addition : ", ans);

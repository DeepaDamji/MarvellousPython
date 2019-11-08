from functools import *;
def compare(no) :
	if no>=70 and no<=90 :
		return True;

def modify(no) :
	return no+10;

def product(no1,no2) : 
	return no1*no2;

print("\n\n****Program Using FMR to Compare Numbers****\n\n");

print("Enter Number of Elements : ");
size=int(input());
arr=list();

print("Enter Elements : ");
for i in range(0, size, 1) : 
	no=int(input());
	arr.append(no);

print("Original List : ", arr);

brr=list(filter(compare, arr));
print("Compared Numbers : ", brr);
crr=list(map(modify, brr));
print("Incremented With 10 : ", crr);
ans=reduce(product,crr);
print("Product of Numbers : ", ans);


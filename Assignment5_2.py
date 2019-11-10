print("\n\n****Recursive Program to Display Numbers****\n\n");

n=5;
def display(n) :
	if n>=1 :
		display(n-1);
		print(n, end=" ");

display(n);
print("\n");

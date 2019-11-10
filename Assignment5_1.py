print("\n\n****Recursive Program to Display Pattern****\n\n");

def display(no) :
	if no==0 :
		return;
	else :
		print("*", end=" ");
		return(display(no-1));

display(5);
print("\n");


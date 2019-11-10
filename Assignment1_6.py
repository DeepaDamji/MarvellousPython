def fun():
	print("Enter a number ");
	num=input();
	if int(num)>0:
		print("Positive Number");
	elif int(num)<0:
		print("Negative Number");
	else: 
		print("Zero");

fun();
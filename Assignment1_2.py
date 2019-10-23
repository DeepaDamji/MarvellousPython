def ChkNum(num):
	res = int(num) % 2;
	
	if res == 0:
		print("Even Number");
	else:
		print("Odd Number");

print("Enter a Number ");
number=input();
ChkNum(number);
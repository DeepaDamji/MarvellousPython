print("\n\n****Program to Multiply 2 Numbers Using Lambda****\n\n");

print("Enter Two Numbers : ");
no1=int(input());
no2=int(input());

res=lambda no1,no2: no1*no2 ;

print("Multiplication is : ", res(no1, no2));
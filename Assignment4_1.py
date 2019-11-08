print("\n\n****Program to Calculate Power Using Lambda****\n\n");

print("Enter a Number : ");
no=int(input());
res=lambda no: no*no

print("Power of ",no," : ",res(no));

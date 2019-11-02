import arithmetic;

print("Enter 2 Numbers ");
num1=input();
num2=input();

print("\n\n****Arithmetic Operations****\n\n");

arithmetic.Add(num1, num2);

res=arithmetic.Sub(num1, num2);
print("Result of Subtraction: ",res);

res=arithmetic.Mul(num1, num2);
print("Result of Multication: ",res);

res=arithmetic.Div(num1, num2);
print("Result of Division: ",res);


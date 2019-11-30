import threading;

def evenFactor(num):
	arr=list();
	for i in range(1, num):
		res=int(num%i);
		if res == 0 :
			if i%2 == 0:
				arr.append(i);
	print("\nEven Factors : ",arr);
	print("Addition of Even Factors : ",sum(arr));

def oddFactor(num):
	arr=list();
	for i in range(1, num):
		res=int(num%i);
		if res == 0 :
			if (i%2) != 0:
				arr.append(i);
	print("\nOdd Factors : ",arr);
	print("Addition of Odd Factors : ",sum(arr));

def exit():
	print("\nExit From Main...");

def main():
	print("\n\n*** Multithreading Program to Display Addition of Even/Odd Factors  ***\n\n")
	num=int(input("Enter Number to Calculate Even & Odd Factors : "));
	t1=threading.Thread(target=evenFactor, args=(num,));
	t2=threading.Thread(target=oddFactor, args=(num,));
	t3=threading.Thread(target=exit);

	t1.start();
	t2.start();
	t3.start();

if __name__ == "__main__":
	main();

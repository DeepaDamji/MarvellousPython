import threading;

def small(input):
	count=0;
	for i in input:
		if i.islower():
			count+=1;
	print("\nThread 1 : Number of Small Characters : ",count);

def capital(input):
	count=0;
	for i in input:
		if i.isupper():
			count+=1;
	print("\nThread 2 : Number of Capital Characters : ",count);

def digit(input):
	count=0;
	for i in input:
		if i.isdigit():
			count+=1;
	print("\nThread 3 : Number of Digits : ",count);

def main():
	print("\n\n*** Multithreading Program to Count Small/ Capital/ Digits in String ***\n\n")
	value=input("Enter Input : ");

	t1=threading.Thread(target=small, args=(value,));
	t2=threading.Thread(target=capital, args=(value,));
	t3=threading.Thread(target=digit, args=(value,));
	
	print("\nMain Thread Details :",threading.main_thread().name, "Id :",threading.currentThread().ident);

	t1.start();
	print("Thread1 Name:", t1.name, "Id :",threading.currentThread().ident);
	t2.start();
	print("Thread2 Name:", t2.name, "Id :",threading.currentThread().ident);
	t3.start();
	print("Thread3 Name:", t3.name, "Id :",threading.currentThread().ident);


if __name__ == "__main__":
	main();
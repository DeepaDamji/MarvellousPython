import threading;

def evenlist(arr):
	sum=0;
	for i in arr:
		if i%2 == 0:
			sum=sum+i;
	print("Thread1 : Addition of Even Parameters : ",sum);

def oddlist(arr):
	sum=0;
	for i in arr:
		if i%2 != 0:
			sum=sum+i;
	print("Thread1 : Addition of Odd Parameters : ",sum);

def main():
	print("\n\n*** Multithreading Program to Display Addition of Even/Odd Elemetnts in List ***\n\n")
	size=int(input("Enter Size of Array : "));
	print("Enter Elements : ");
	arr=list();
	for i in range(0, size):
		number=int(input());
		arr.append(number);

	t1= threading.Thread(target=evenlist, args=(arr,));
	t2= threading.Thread(target=oddlist, args=(arr,));

	t1.start();
	t2.start();

if __name__ == "__main__":
	main();






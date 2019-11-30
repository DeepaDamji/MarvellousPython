import threading;
def even():
	for i in range(1,10):
		if i%2 == 0:
			print("Even : ",i);

def odd():
	for i in range(1,10):
		if i%2 != 0:
			print("Odd : ",i);

def main():
	print("\n\n*** Multithreading Program to Display First 10 Even/Odd Numbers ***\n\n")
	t1 = threading.Thread(target=even); 
	t2 = threading.Thread(target=odd);

	t1.start();
	t2.start();

if __name__ == "__main__":
	main();

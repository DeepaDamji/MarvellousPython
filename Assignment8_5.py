from os import *;
from time import *;
from multiprocessing import *;
import threading;

def thread1(lobj):
	print("\n");
	sleep(5);
	lobj.acquire();
	for i in range(1, 51):
		print("Thread 1:", i);
	lobj.release();	
	print("\n");

def thread2(lobj):
	print("\n")
	lobj.acquire();
	for i in range(50, 0, -1):
		print("Thread 2:", i);
	lobj.release();
	print("\n");
	
def main():
	lobj=Lock();

	print("\n\n*** Multithreading Program to Using Lock Object ***")

	t1=threading.Thread(target=thread1, args=(lobj,));
	t1.start();

	t2=threading.Thread(target=thread2, args=(lobj,));
	t2.start();
	
	t1.join();
	t2.join();

if __name__ == "__main__":
	main();

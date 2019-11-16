class BookStore:
	noOfBooks=0;

	def __init__(self,name,author):
		self.name=name;
		self.author=author;
		BookStore.noOfBooks+=1;

	def display(self):
		print(self.name," by ",self.author,".   ", "No of Books : ",BookStore.noOfBooks);

def main():
	print("\n\n*** OOP (Encapsulation) Program to Display Book Details ***\n\n")
	obj1=BookStore("Linux System Programming","Robert Love");
	obj1.display(); 

	obj2=BookStore("C Programming","Dennis Ritchie");
	obj2.display();

if __name__ == "__main__":
	main();



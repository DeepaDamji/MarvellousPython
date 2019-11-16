class Circle():
    pi = 3.14;

    def __init__(self):
    	radius=0.0;
    	area=0.0;
    	circumference=0.0;

    def accept(self):
    	print("Enter Radius to Calculate Area and Circumference : ");
    	radius=float(input());
    	self.radius = radius;

    def area(self):
        self.area = Circle.pi * self.radius * self.radius;

    def circumference(self):
    	self.circumference = Circle.pi * self.radius * 2;

    def display(self):
    	print("Entered Radius : ",self.radius);
    	print("Area of Circle : ",self.area);
    	print("Circumference of Circle : ",self.circumference);

def main():
	Circle.pi
	c = Circle()
	
	print("\n\n***OOP (Encapsulation) Program to calculate Area and Circumference of Circle***\n\n")
	c.accept();
	c.area()
	c.circumference();
	c.display();

if __name__ == "__main__":
	main();





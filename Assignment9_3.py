import sys;
import os;

def main():
	if len(sys.argv)<2 or len(sys.argv)>2:
		print("\nInvalid Argument");
		print("To know usage of program, use -u command\n");
		exit();

	if sys.argv[1] == "-h" or sys.argv[1] == "-H":
		print("\nThis program is written to content of one file to another");
		print("To know usage of program, use -u command\n");
		exit();

	if sys.argv[1] == "-u" or sys.argv[1] == "-U":
		print("\npython <program_name> <file_name>");
		print("<program_name> : Name of program");
		print("<fil_name> : Name of file\n");
		exit();

	else:
		fobj1=open(sys.argv[1],"r");
		fobj2=open("Demo.txt","w+");
		print("\nCopied Contents of ABC.txt to Demo.txt")
		print("Displaying Contents of Demo.txt file\n");
		for line in fobj1:
			fobj2.write(line);
		fobj2.close();
		
		fobj2=open("Demo.txt","r");
		print(fobj2.read());
		fobj2.close();

		fobj1.close();

if __name__ == "__main__":
	main();
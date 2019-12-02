import sys;
import os;

def main():
	if len(sys.argv)<2 or len(sys.argv)>2:
		print("\nInvalid Argument");
		print("To know usage of program, use -u command\n");
		exit();

	if sys.argv[1] == "-h" or sys.argv[1] == "-H":
		print("\nThis program is written to open given file in read mode");
		print("To know usage of program, use -u command\n");
		exit();

	if sys.argv[1] == "-u" or sys.argv[1] == "-U":
		print("\npython <program_name> <file_name>");
		print("<program_name> : Name of program");
		print("<fil_name> : Name of file\n");
		exit();

	else:
		fobj=open(sys.argv[1],"r");
		#print(fobj);
		
		print("\nContents of File \n");
		print(fobj.read());
		
		fobj.close();	

if __name__ == "__main__":
	main();
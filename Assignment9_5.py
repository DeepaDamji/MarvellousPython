import sys;
import os;

def main():
	if len(sys.argv)<2 or len(sys.argv)>3:
		print("\nInvalid Argument");
		print("To know usage of program, use -u command\n");
		exit();

	if sys.argv[1] == "-h" or sys.argv[1] == "-H":
		print("\nThis program is written to find frequency of given string in file");
		print("To know usage of program, use -u command\n");
		exit();

	if sys.argv[1] == "-u" or sys.argv[1] == "-U":
		print("\npython <program_name> <string>");
		print("<program_name> : Name of program");
		print("<string> : Any string\n");
		exit();

	else:
		fobj=open(sys.argv[1],"r");
		count=0;
		line=fobj.read();
		string=line.split();
		
		for i in string:
			if i==sys.argv[2]:
				count+=1;

		print("Frequency of Given String:", count);

		fobj.close();

if __name__ == "__main__":
	main();


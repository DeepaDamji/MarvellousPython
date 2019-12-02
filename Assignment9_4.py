import sys;
import filecmp;

def main():
	if len(sys.argv)<2 or len(sys.argv)>3:
		print("\nInvalid Argument");
		print("To know usage of program, use -u command\n");
		exit();

	if sys.argv[1] == "-h" or sys.argv[1] == "-H":
		print("\nThis program is written to compare two files to check if they are identical or not");
		print("To know usage of program, use -u command\n");
		exit();

	if sys.argv[1] == "-u" or sys.argv[1] == "-U":
		print("\npython <program_name> <file_name_1> <file_name_2>");
		print("<program_name> : Name of program");
		print("<file_name> : Name of file\n");
		exit();

	else:
		res=filecmp.cmp(sys.argv[1],sys.argv[2])
		if res==True :
			print("Success! Contents of Both Files are Same");
		else :
			print("Failure! Contents of Both Files are Different");

if __name__ == "__main__":
	main();

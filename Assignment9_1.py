import sys;
import os;

def main():
	if len(sys.argv)<2 or len(sys.argv)>2:
		print("\nInvalid Argument");
		print("To know usage of program, use -u command\n");
		exit();

	if sys.argv[1] == "-h" or sys.argv[1] == "-H":
		print("\nThis program is written to check whether the file exists in current directory");
		print("To know usage of program, use -u command\n");
		exit();

	if sys.argv[1] == "-u" or sys.argv[1] == "-U":
		print("\npython <program_name> <file_name>");
		print("<program_name> : Name of program");
		print("<fil_name> : Name of file\n");
		exit();

	else:
		path=os.path.dirname(os.path.realpath(sys.argv[1]));
		count=0;
		for folder, subfolder, file in os.walk(path):
			if sys.argv[1] in file:
				count=count+1;
				filepath=os.path.join(folder, sys.argv[1]);
				print("\nFile Exists in Directory :", filepath);
		if count==0:
			print("Given File Doesn't Exists...");

if __name__ == "__main__":
	main();
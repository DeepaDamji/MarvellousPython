import sys;
import os;
import psutil;
import time;

def processDisplay(path):
	line="-"*90;
	print("Running Processes are Displayed to Log File");

	if not os.path.exists(path):
		os.mkdir(path);
	
	filename = os.path.join(path,"Log.txt");
	#filename=os.path.join(path, "Log%s.txt"%time.ctime());
	print(filename);
	fobj=open(filename,"w");

	fobj.write(line+"\n");
	fobj.write("Process Logger at : %s\n"%time.ctime());
	fobj.write(line+"\n");

	for pobj in psutil.process_iter():
		print(pobj);
		fobj.write("\n"+str(pobj));

	fobj.close();

def main():
	print("_"*78);
	print("\nAuthor     : Program is Developed by Deepa Damji");
	print("Description: Python Program to Display All Running Processes");
	print("Date & Time: 2019-12-12 04:00:00");
	print("_"*78,"\n");

	processDisplay(sys.argv[1]);

if __name__ == "__main__":
	main();
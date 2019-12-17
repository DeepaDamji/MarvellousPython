import sys;
import os;
import time;
import psutil;

def processDisplay(path):
	
	if not os.path.exists(path):
		try:
			os.mkdir(path);
		except Exception:
			pass;

	line="-"*90;
	newpath=os.path.join(path, "Log.log");
	fobj=open(newpath, "w");
	fobj.write(line+"\n");
	fobj.write("Process Logger at : %s\n"%time.ctime());
	fobj.write(line+"\n");

	flag=0;
	try:
		for pobj in psutil.process_iter():
			flag=1;
			process=pobj.as_dict(attrs=['pid', 'name','username']);
			fobj.write("\n"+str(process));
	except Exception as e:
		fobj.write(str(e));

	if flag==1:
		print("Processes are Displayed to Log File");
	else:
		print("Error to Display Running Processes. Watch Log File ")
	
def main():
	print("_"*78);
	print("\nAuthor     : Program is Developed by Deepa Damji");
	print("Description: Python Program to Display Processes in Log File of Given Directory");
	print("Date & Time: 2019-12-12 04:00:00");
	print("_"*78,"\n");

	processDisplay(sys.argv[1]);

if __name__ == "__main__":
	main();
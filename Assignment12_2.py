import sys;
import os;
import psutil;
import time;

def processDisplay(inputprocess):
	line="-"*90;
		
	fobj=open("Log.txt","w");

	fobj.write(line+"\n");
	fobj.write("Process Logger at : %s\n"%time.ctime());
	fobj.write(line+"\n");

	listprocess=[];
	flag=0;
	try:
		inputprocess=inputprocess+".exe";
		for pobj in psutil.process_iter():
			process= pobj.as_dict(attrs=['name'])
			
			if process['name'] == inputprocess.casefold():
				flag=1;
				pinfo=pobj.as_dict(attrs=['pid','name','username']);
				fobj.write("\n"+str(pinfo));
		
		if flag==0:
			print("Process is Not Running");
		else:
			print("Process Informaion is saved to Log File");
			
	except Exception as e:
		print(e);

	fobj.close();

def main():
	print("_"*78);
	print("\nAuthor     : Program is Developed by Deepa Damji");
	print("Description: Python Program to find running process");
	print("Date & Time: 2019-12-12 04:00:00");
	print("_"*78,"\n");

	processDisplay(sys.argv[1]);

if __name__ == "__main__":
	main();
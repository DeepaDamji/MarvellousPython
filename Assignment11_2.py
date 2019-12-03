import sys
import os
import hashlib
import logging

def hashfile(path, blocksize=1024):
	afile=open(path,'rb');
	hasher=hashlib.md5();
	buf=afile.read(blocksize);
	while len(buf) > 0:
		hasher.update(buf);
		buf=afile.read(blocksize);
	afile.close();
	return hasher.hexdigest();

def findDuplicate(path):
	flag=os.path.isabs(path);
	if flag == False:
		path=os.path.abspath(path);

	exists=os.path.isdir(path);

	dups={};

	if exists:
		for dirname, subdir, filelist in os.walk(path):
			print("Current Folder:", dirname);
			for filen in filelist:
				path=os.path.join(dirname,filen);
				file_hash=hashfile(path);
				if file_hash in dups:
					dups[file_hash].append(path);
				else:
					dups[file_hash]=[path];
		return dups;
	else:
		logging.info("Error: Invalid Path");

def displayDuplicate(dupsDict):
	results=list(filter(lambda x: len(x)>1, dupsDict.values()));

	if len(results)>0:
		print("Found Duplicate Files");
		logging.info("List of Duplicate Files:");

		count=0;
		for result in results:
			for subresult in results:
				count+=1;
				if count>1:
					logging.info(subresult);
		
	else:
		logging.info("No duplicate Files Found");

	
def main():
	print("_"*78);
	print("\nAuthor     : Program is Developed by Deepa Damji");
	print("Description: Python Program to find duplicate files in directory");
	print("Date & Time: 2019-12-3 08:00:00");
	print("_"*78,"\n");

	logging.basicConfig(filename="Log.txt", format='%(asctime)s %(levelname)s: %(message)s', filemode='w', level=logging.INFO);

	if len(sys.argv)!=2:
		logging.info("Error: Invalid Number of Arguments");

	if sys.argv[1] == "-h" or sys.argv[1] == "-H":
		print("\nThis program is written to find duplicate files");
		print("To know usage of program, use -u command\n");
		exit();

	if sys.argv[1] == "-u" or sys.argv[1] == "-U":
		print("\npython <application_name> <AbsolutePath_of_directory>");
		print("<Application_name> : Name of Application");
		print("<AbsolutePath_of_directory> : Absolute Path\n");
		exit();

	try:
		arr={};
		arr=findDuplicate(sys.argv[1]);
		displayDuplicate(arr);

	except ValueError:
		logging.info("Error: Invalid datatype of input");

	except Exception as e:
		logging.info("Error: Invalid input",e);

if __name__ == "__main__":
	main();


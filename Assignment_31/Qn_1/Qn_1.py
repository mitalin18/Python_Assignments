'''
Please follow below rules while designing automation script as
. Accept input through command line or through file.
. Display any message in log file instead of console.
. For separate task define separate function.
. For robustness handle every expected exception.
. Perform validations before taking any action.
. Create user defined modules to store the functionality.

1. Design automation script which accept directory name and file extension from user Display all files with that extension.
Usage DirectoryFileSearch.py "Demo" ".txt"
Demo is name of directory and .txt is the extension that we want to search'''

import os
import sys
import time

def DirectoryScanner(DirectoryName, Extension):
    Border = "-"*50
    timestamp = time.ctime()

    logfilename = "Demo%s.log" %(timestamp)
    logfilename = logfilename.replace(" ","_")
    logfilename = logfilename.replace(":","_")

    fobj = open(logfilename,"w")
    fobj.write(Border + "\n")
    fobj.write("This is a log file created by Mitali\n")
    fobj.write("This script displays all files with the given extension\n")
    fobj.write(Border+"\n")

    Ret = False
    Ret =os.path.exists(DirectoryName)

    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("Unable to scan as it is not a directory")
        return
    
    FileCount = 0
    MatchedCount = 0

    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):
        for fname in FileName:
            FileCount +=1
            if fname.endswith(Extension):
                MatchedCount+=1
                fullpath = os.path.join(FolderName,fname)
                fobj.write("File Found : " + fullpath + "\n")

    fobj.write(Border + "\n")
    fobj.write(f"Total files scanned :  {FileCount} \n")
    fobj.write(f"Total matching files : {MatchedCount} \n")
    fobj.write(f"Log file created at :  {timestamp}\n")
    fobj.write(Border + "\n")

    
    fobj.write(Border + "\n")
    fobj.write("-------------------- Thank you -------------------" + "\n")

    fobj.close()


def main():
    if len(sys.argv)!=3:
        print("Invalid number of arguments")
        return
    
    DirectoryScanner(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()
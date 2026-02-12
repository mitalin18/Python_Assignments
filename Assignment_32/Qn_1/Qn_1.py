'''Please follow below rules while designing automation script as

. Accept input through command line or through file.
. Display any message in log file instead of console.
. For separate task define separate function.
. For robustness handle every expected exception.
. Perform validations before taking any action.
. Create user defined modules to store the functionality.

1. Design automation script which accept directory name and display checksum of all files.
Usage : DirectoryChecksum.py "Demo"
Demo is name of directory.'''

import os
import sys
import hashlib
import time



def CalculateChecksum(path):
    fobj=open(path,"rb")
    hobj= hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    return hobj.hexdigest()

def DirectoryChecksum(DirectoryName):
    Border = "-" * 50
    timestamp = time.ctime()

    # Create log file
    logfilename = "ChecksumLog_%s.log" %(timestamp)
    logfilename = logfilename.replace(" ", "_")
    logfilename = logfilename.replace(":", "_")

    fobj = open(logfilename, "w")
    fobj.write(Border + "\n")
    fobj.write("This is a log file created by Mitali\n")
    fobj.write("Directory Checksum Script\n")
    fobj.write(Border + "\n")

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


    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        for fname in FileName:
            fullpath = os.path.join(FolderName, fname)
            try:
                checksum = CalculateChecksum(fullpath)
                FileCount += 1
                fobj.write(f"{fullpath} : {checksum}\n")

            except Exception as e:
                fobj.write(f"Unable to process {fullpath} : {e}\n")

    fobj.write(Border + "\n")
    fobj.write(f"Total files scanned : {FileCount}\n")
    fobj.write("Log created at : " + timestamp + "\n")
    fobj.write(Border + "\n")

    fobj.close()



def main():

    Border = "-" * 50
    print(Border)
    print("----- Directory Checksum Automation ----")
    print(Border)

    if len(sys.argv)!= 2:
        print("Invalid number of arguments")
        return
    
    DirectoryChecksum(sys.argv[1])

    print(Border)
    print("-------------- Thank you --------------")
    print(Border)

if __name__ == "__main__":
    main()
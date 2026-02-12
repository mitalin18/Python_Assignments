''' Design automation script which accept directory name and write names of duplicate files from
that directory into log file named as Log.txt. Log.txt file should be created into current
directory.

Usage : DirectoryDusplicate.py "Demo"

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
    fobj.write("Duplicate files detection Script\n")
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
    files_dict = {}



    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        for fname in FileName:
            fullpath = os.path.join(FolderName, fname)
            try:
                checksum = CalculateChecksum(fullpath)

                if checksum in files_dict:
                    files_dict[checksum].append(fullpath)

                else:
                    files_dict[checksum] = [fullpath]

            except Exception as e:
                fobj.write(f"Unable to process {fullpath} : {e}\n")

    DuplicateFound = False

    for checksum, filelist in files_dict.items():
        if len(filelist) >1:
            DuplicateFound = True
            fobj.write("\nDuplicate Files\n")
            for file in filelist:
                fobj.write(file + "\n")
    
    if not DuplicateFound:
        fobj.write("No duplicate files found")

    fobj.write(Border + "\n")

    fobj.close()



def main():

    Border = "-" * 50
    print(Border)
    print("----- Duplicate Files Report ----")
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
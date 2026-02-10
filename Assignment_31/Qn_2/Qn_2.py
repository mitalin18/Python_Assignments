'''2. Design automation script which accept directory name and two file extensions from user.
Rename all files with first file extension with the second file extenntion.

Usage : DirectoryRename.py "Demo" ".txt" ".doc"

Demo is name of directory and .txt is the extension that we want to search and rename
with .doc.
After execution this script each .txt file gets renamed as .doc.'''

import os
import sys
import time

def DirectoryScanner(DirectoryName, OldExtension, NewExtension):
    Border = "-"*50
    timestamp = time.ctime()

    logfilename = "Demo%s.log" %(timestamp)
    logfilename = logfilename.replace(" ","_")
    logfilename = logfilename.replace(":","_")

    fobj = open(logfilename,"w")
    fobj.write(Border + "\n")
    fobj.write("This is a log file created by Mitali\n")
    fobj.write("This script renames all files with the given extension with desired extension\n")
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
    
    RenameCount = 0
    FileCount = 0

    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):
        for fname in FileName:
            FileCount +=1
            if fname.endswith(OldExtension):
                old_path = os.path.join(FolderName,fname)
                new_name = fname.replace(OldExtension,NewExtension)
                new_path = os.path.join(FolderName,new_name)

                os.rename(old_path, new_path)
                RenameCount+=1


                fobj.write(f"Renamed : {old_path} to - {new_path} \n")

    fobj.write(Border + "\n")
    fobj.write(f"Total files scanned :  {FileCount} \n")
    fobj.write(f"Total files Renamed : {RenameCount} \n")
    fobj.write(f"Log file created at :  {timestamp}\n")
    fobj.write(Border + "\n")

    
    fobj.write(Border + "\n")
    fobj.write("-------------------- Thank you -------------------" + "\n")

    fobj.close()


def main():

    if len(sys.argv)!=4:
        print("Invalid number of arguments")
        return
    
    DirectoryScanner(sys.argv[1],sys.argv[2], sys.argv[3])


if __name__ == "__main__":
    main()
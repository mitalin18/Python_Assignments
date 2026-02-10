''' Design automation script which accept two directory names. Copy all files from first directory
into second directory. Second directory should be created at run time.
Usage : DirectoryCopy.py "Demo" "Temp"
Demo is name of directory which is existing and contains files in it. We have to create new
Directory as Temp and copy all files from Demo to Temp.
'''
import os
import shutil
import sys
import time

def DirectoryCopy(SourceDir, DestDir):
    Border = "-"*50
    timestamp = time.ctime()

    logfilename = "Demo_%s.log" %(timestamp)
    logfilename = logfilename.replace(" ","_")
    logfilename = logfilename.replace(":","_")

    fobj = open(logfilename,"w")
    fobj.write(Border + "\n")
    fobj.write("This is a log file created by Mitali\n")
    fobj.write("This script Copies all files from first directory into second directory\n")
    fobj.write(Border+"\n")

    Ret = False
    Ret =os.path.exists(SourceDir)

    if(Ret == False):
        print("There is no source directory\n")
        return
    
    Ret = os.path.isdir(SourceDir)

    if(Ret == False):
        print("Source path is not a directory\n")
        return
    
    if not os.path.exists(DestDir):
        os.mkdir(DestDir)
        fobj.write("Destination Directory created\n")

    FileCount = 0

    for FolderName,SubFolderName,FileName in os.walk(SourceDir):
        for fname in FileName:
                Source_path = os.path.join(FolderName,fname)
                Dest_Path= os.path.join(DestDir,fname)
                if os.path.exists(Dest_Path):
                    fobj.write(f"Skipped (Already exists) : {Dest_Path} \n")
                else:
                    shutil.copy(Source_path,Dest_Path)
                    FileCount+=1
                    fobj.write(f"Copied : {Source_path} to - {Dest_Path} \n")

    fobj.write(Border + "\n")
    fobj.write(f"Total files Copied : {FileCount} \n")
    fobj.write(f"Log file created at :  {timestamp}\n")
    fobj.write(Border + "\n")

    
    fobj.write(Border + "\n")
    fobj.write("-------------------- Thank you -------------------" + "\n")

    fobj.close()


def main():

    if len(sys.argv)!=3:
        print("Invalid number of arguments")
        print("Usage : DirectoryCopy.py SourceDir DestDir")

        return
    
    DirectoryCopy(sys.argv[1],sys.argv[2])


if __name__ == "__main__":
    main()

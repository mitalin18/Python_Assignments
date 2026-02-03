'''Check File Exists in Current Directory

Problem Statement:
Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.

Input:
Demo.txt

Expected Output:
Display whether Demo.txt exists or not
'''

import os
import sys

def DirectoryScanner(DirectoryName = "Demo"):
    Ret = False
    Ret = os.path.exists(DirectoryName)
    if (Ret == False):
        print("There is no such directory.")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    for FolderName, SubFolderName,FileName in os.walk(DirectoryName):
        for fname in FileName:
            print(fname)


def main():

    if(len(sys.argv)) != 2:
       print("Invalid number of arguments")
       print("Please specify the name of directory")
       return
    DirectoryScanner(sys.argv[1])


if __name__ == "__main__":
    main()


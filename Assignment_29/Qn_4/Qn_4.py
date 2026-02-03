'''Compare Two Files (Command Line)
Problem Statement:
Write a program which accepts two file names through command line arguments and compares the contents of both files.
If both files contain the same contents, display Success
Otherwise display Failure
Input (Command Line): Demo.txt Hello.txt
Expected Output:
Success OR Failure
'''

import sys

def main():
    try:
        fileOne = sys.argv[1]
        fileTwo = sys.argv[2]

        fone = open(fileOne,"r")
        data1 = fone.read()
        fone.close()


        ftwo = open(fileTwo,"r")
        data2 = ftwo.read()
        ftwo.close()

        if(data1 == data2):
            print("Success")
        else:
            print("Failure")
    
    except FileNotFoundError:
        print("File does not exist")
    
    finally:
        print("End of the application")



if __name__ == "__main__":
    main()


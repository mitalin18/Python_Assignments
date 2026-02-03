'''Copy File Contents into a New File (Command Line)
Problem Statement:
Write a program which accepts an existing file name through command line arguments creates a new file named Demo.txt 
and copies all contents from the given file into Demo.txt
Input (Command Line):
ABC.txt
Expected Output:
Create Demo txt and copy contents of ABC.txt into Demo.txt
'''

import sys

def main():
    try:

        source_file = sys.argv[1]

        fsrc = open(source_file,"r")
        print("Source file is opened.")

        data = fsrc.read()
        fsrc.close()
        
        fobj=open("Demo.txt","w")
        fobj.write(data)
        fobj.close()

        print("Content has been copied successfully to Demo.txt")

    except IndexError:
        print("Provide file name from command line")

    except FileNotFoundError:
        print("Source file does not exist.")

    finally:
        print("End of the application")


if __name__ == "__main__":
    main()
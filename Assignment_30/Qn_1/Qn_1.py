'''Count Lines in a File
Problem Statement:
Write a program which accepts a file name from the user and counts how many lines are present in the file
Input:
Demo.txt
Expected Output:
Total number of lines in Demo.txt
'''

def main():
    try:
        fname = input("Enter the name of file : ")

        fobj = open(fname,"r")
        lines = fobj.readlines()
        nooflines = len(lines)
        fobj.close()
        print("Number of lines : ", nooflines)

    except FileNotFoundError:
        print("there is no such file.")

    finally:
        print("End of an application!")

if __name__ == "__main__":
    main()
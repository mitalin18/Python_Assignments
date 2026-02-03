'''Display File Line by Line

Problem Statement:
Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen
Input:
Demo.txt
Expected Output:
Display each line of Demo.txt one by one
'''

def main():
    filename = input("Enter the file name :")
    fobj = open(filename,"r")
    lines = fobj.readlines()
    fobj.close()
    print("Content of the file : ",lines)


if __name__ == "__main__":
    main()
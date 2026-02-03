'''Display File Contents
Problem Statement:
Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console
Input:
Demo.txt
Expected Output:
Display contents of Demo.txt on console
'''


def main():
    try:
        fobj = open("Demo.txt","r")
        print("File gets successfully opened!")

        Data = fobj.read()
        print("Data from the file is : ", Data)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of an application.")



if __name__ =="__main__":
    main()
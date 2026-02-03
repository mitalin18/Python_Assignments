'''Copy File Contents into Another File
Problem Statement:
Write a program which accepts two file names from the user.
First file is an existing file
Second file is a new file
Copy all contents from the first file into the second file.
Input:
ABC.txt Demo.txt
Expected Output:
Contents of ABC.txt copied into Demo.txt
'''

def main():
    try:

        source_file = input("Enter the file name")
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










'''Count Words in a File

Problem Statement:
Write a program which accepts a file name from the user and counts the total number of words in that file
Input:
Demo.txt
Expected Output:
Total number of words in Demo.txt
'''

def main():
    try: 
        filename = input("Enter the name of file: ")
        fobj = open(filename,"r")
        data= fobj.read()
        fobj.close()
        words = data.split()
        #data = fobj.read().split()
        wordscount = len(words)
        print(f"Total number of words are {wordscount}")
    
    except FileNotFoundError:
        print("File not found")

    finally:
        print("End of the application.")


if __name__ == "__main__":
    main()
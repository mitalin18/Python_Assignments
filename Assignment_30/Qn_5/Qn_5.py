'''Search a Word in File

Problem Statement:
Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not
Input:
Demo.txt Marvellous
Expected Output:
Display whether the word Marvellous is found in Demo.txt or not'''

def main():
    try:
        filename = input("Enter the file name :")
        strtofind = input("Enter the word to find :")

        fobj = open(filename,"r")
        data = fobj.read()
        fobj.close()
        words = data.split()

        if strtofind in words:
            print(f"The word {strtofind} is present in the file" )

        else:
            print(f"The word {strtofind} is not present in the file")

        
    

    except FileNotFoundError:
        print("File not found")
    

if __name__ == "__main__":
    main()
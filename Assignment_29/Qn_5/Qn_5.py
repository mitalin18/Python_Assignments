'''Frequency of a String in File
Problem Statement:
Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) 
of that string in the file
Input:
Demo.txt Marvellous
Expected Output:
Count how many times "Marvellous" appears in Demo.txt'''



import sys


def main():
    try:
        filename = sys.argv[1]
        strtofind = sys.argv[2]

        fobj = open(filename,"r")
        data = fobj.read()
        fobj.close()
        
        result = data.count(strtofind)
        print(f"The frequency of {strtofind} is {result}")

    except FileNotFoundError:
        print("File not found")
    

if __name__ == "__main__":
    main()
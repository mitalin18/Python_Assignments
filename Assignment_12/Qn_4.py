# Write a program which accepts one number and prints that many numbers starting from 1. Input: 5  Output : 12345

def PrintAllNo(no):
    for i in range(1, no + 1):
        print (i, end = "")



def main():
    no = int(input("Enter the number : "))
    PrintAllNo(no)

if __name__ == "__main__":
    main()
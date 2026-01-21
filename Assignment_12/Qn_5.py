#  Write a program which accepts one number and prints that many numbers in reverse order Input: 5 Output: 54321

def PrintReverseTillNo(no):
    for i in range(no , 0, -1):
        print(i , end = "")

def main():
    no = int(input("Enter the number : "))
    PrintReverseTillNo(no)

if __name__ == "__main__":
    main()
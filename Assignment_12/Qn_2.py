# Write a program which accepts one number and prints its factors. Input: 12  Output: 1 2 3 4 6 12

def PrintFact(no):
    for i in range(1,no + 1):
        if no % i == 0:
            print(i)

def main():
    no = int(input("Enter the number : "))
    PrintFact(no)

if __name__ == "__main__":
    main()

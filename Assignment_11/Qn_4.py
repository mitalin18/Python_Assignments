# Write a program which accepts one number and prints reverse of that number. Input: 123 Output: 321

def PrintRev(no):
    rev = 0
    while no > 0:
        digit = no % 10
        rev = rev * 10  + digit
        no = no // 10
    print("Reverse is : ", rev)

def main():
    no = int(input("Enter the number : "))
    PrintRev(no)

if __name__ == "__main__":
    main()
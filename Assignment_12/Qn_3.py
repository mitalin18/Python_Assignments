# Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.


def PrintOper(no1,no2):
    sum = 0
    sub = 0
    mul = 0
    div = 0

    sum = no1 + no2
    print("Addition is : ", sum)

    sub = no1 - no2
    print("Subtraction is :", sub)

    mul = no1 * no2
    print("Multiplication is :", mul)

    div = no1 / no2
    print("Division is :", div)




def main():
    no1 = int(input("Enter first number :"))
    no2 = int(input("Enter second number :"))
    PrintOper(no1,no2)

if __name__ == "__main__":
    main()
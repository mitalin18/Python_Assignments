# Write a program which accepts one number and prints sum of digits. Input: 123 Output: 6


def SunOfDigits(no):
    sum = 0
    while no > 0:
        digit = no % 10
        sum = sum + digit
        no = no // 10

    print(sum)


def main():
    no = int(input("Enter number : "))
    SunOfDigits(no)


if __name__ == "__main__":
    main()
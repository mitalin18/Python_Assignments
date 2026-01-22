# Write a lambda function which accepts two numbers and returns maximum number.

PrintMax = lambda no1, no2: no1 if no1 > no2 else no2

def main():
    no1 = int(input("Enter the first number : "))
    no2 = int(input("Enter the second number : "))
    maxnumber  = PrintMax(no1, no2)
    print(maxnumber)

if __name__ == "__main__":
    main()
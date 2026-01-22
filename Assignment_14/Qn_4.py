# Write a lambda function which accepts two numbers and returns minimum number


PrintMin = lambda no1,no2 : no1 if no1< no2 else no2

def main():
    no1 = int(input("Enter the first number : "))
    no2 = int(input("Enter the second number : "))
    result = PrintMin(no1, no2)
    print(result)

if __name__ == "__main__":
    main()
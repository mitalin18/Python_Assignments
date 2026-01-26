''' Write a program which contains one lambda function which accepts two parameters and return its multiplication.
Input 4 3
Input 6 3
Output 12
Output 18
'''

multiplication = lambda a, b: a * b

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    result = multiplication(x, y)
    print(result)

if __name__ == "__main__":
    main()

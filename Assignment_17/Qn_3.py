'''Write a program which accept one number from user and return its factorial.
Input 5
Output 120 '''

def fact(No):
    res = 1
    for i in range(1, No + 1):
        res = i * res
    print(res)

def main():
    No = int(input("Enter the number : "))
    fact(No)

if __name__ == "__main__":
    main()


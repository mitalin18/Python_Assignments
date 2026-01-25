'''Write a program which accept number from user and return number of digits in that number
Input 5187934
Output 7'''

def CountNum(no):
    count = 0
    while no > 0:
        count = 1 + count
        no = no // 10
    print(count)

def main():
    no = int(input("enter the number : "))
    CountNum(no)

if __name__ == "__main__":
    main()


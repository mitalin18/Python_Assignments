''' 2. Write a program which accepts one number and prints sum of first N natural numbers. Input: 5 Output: 15 '''

def SumNum(no):
    total = 0
    for i in range(1, no + 1 ):
        total = total  + i
    
    print(total)


def main():
    no = int(input("Enter the number to print sum of first N numbers : "))
    SumNum(no)


if __name__ == "__main__":
    main()
'''Write a program which accept one number form user and return addition of its factors.
12 Input
Output 16
(1+2+3+4+6)'''


def AddFact(No):
    total = 0 
    for i in range(1, No):
        if No % i == 0:
            total = total + i
    return total
        
def main():
    No = int(input("Enter the number :"))
    result = AddFact(No)
    print(result)

if __name__ == "__main__":
    main()

# Write a program which accepts one number and prints count of digits in that number. Input: 7521 Output: 4 


def GetCountOfDigit(no):
    Count = 0 
    while no > 0:
        Count = Count + 1
        no = no // 10
    
    print( Count)



def main():
    no = int(input("Enter the number : "))
    GetCountOfDigit(no)

if __name__ == "__main__":
    main()
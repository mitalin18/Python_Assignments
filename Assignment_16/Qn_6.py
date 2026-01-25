''' Write a program which accept number from user and check whether that number is positive or negative or zero. 
Input 11
Output Positive Number
input -1
Output Negative Number
Input 0
Output Zero
'''


def ChkPositive(no):
    if no > 0:
        print("Positive number")
    elif no < 0:
        print("Negative Number")
    elif no == 0:
        print("Zero")

def main():
    no = int (input("Ente rthe number : "))
    ChkPositive(no)

if __name__ == "__main__":
    main()




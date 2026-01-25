'''Write a program which contains one function named as ChkNum() which accept one parameter as number. 
If number is even then it should display "Even number otherwise display "Odd number" on console.

Input 11

Input 8'''


def ChkNum(no):
    if no % 2 == 0 :
        print("Even Number")
    else:
        print("Odd Number")

def main():
    no = int(input("Enter the number : "))
    ChkNum(no)

if __name__ == "__main__":
    main()

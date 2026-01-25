'''Write a program which accept number from user and print that number of "*" on screen.
Input 5
Output * * * * *
'''

def printstar(no):
    for i in range(no):
        print("*" ,end=" ")

def main():
    no = int(input("Enter the no of times you want : "))
    printstar(no)

if __name__ == "__main__":
    main()

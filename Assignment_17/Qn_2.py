'''Write a program which accept one number and display below pattern.  I / P = 5 5
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

def printstar(row,column):
    for i in range(row):
        for j in range(column):
            print("*", end= "")
        print("")

def main():
    row = int(input("Enter no of rows :"))
    column = int(input("Enter no of columns :"))
    printstar(row,column)

if __name__ == "__main__":
    main()

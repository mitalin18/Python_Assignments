'''Write a program which accept one number and display below pattern. 5

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''

def printstar(row):
    for i in range(row):
        for j in range(1, row + 1):
            print(j, end= " ")
        print("")

def main():
    row = int(input("Enter the number :"))
    printstar(row)

if __name__ == "__main__":
    main()

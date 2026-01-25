'''Write a program which accept one number and display below pattern. 

Input 5
Output
1
12
123
1234
12345
'''

def printstar(row):
    for i in range(row +1):
        for j in range(1, i+1):
            print(j, end= " ")
        print("")

def main():
    row = int(input("Enter the number :"))
    printstar(row)

if __name__ == "__main__":
    main()

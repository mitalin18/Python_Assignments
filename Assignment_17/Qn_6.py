'''Write a program which accept one number and display below pattern.
Output 5 
*****
****
***
**
*
'''

def printstar(row):
    for i in range(row,0,-1):
        for j in range(i):
            print("*", end= "")
        print("")

def main():
    row = int(input("Enter no of rows :"))
    printstar(row)

if __name__ == "__main__":
    main()

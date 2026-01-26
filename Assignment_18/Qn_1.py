'''Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.

Input Number of elements 6
Input Elements 13 5 45 7 4 56

Output 130
'''

def AddElements(Elements):
    Total = 0
    for i in Elements:
        Total = Total + i 
    return Total

def main():
    NoOfElements = int(input("Enter the number of elements :"))
    Data = []

    print("Enter Elements")
    for i in range(NoOfElements):
        value = int(input())
        Data.append(value)

    result = AddElements(Data)
    print(result)
  

if __name__ == "__main__":
    main()

# Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers

from functools import reduce

TotalEven = lambda no : no % 2 == 0

def main():
    count = 0
    Data = [1,2,3,4,5,6,7,8,9,10]
    print("Original data is : ", Data)

    FData = list(filter(TotalEven,Data))
    count = len(FData)
    print("Count of even numbers is : ", count)

if __name__ == "__main__":
    main()
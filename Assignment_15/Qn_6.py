#  Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element

from functools import reduce

GetMin = lambda A, B: A if A < B else B


def main():
    Data = [10,55,23,59,34,22]
    print("Original Data is :",Data)

    RData = reduce (GetMin,Data)
    print("Minimum Number is :", RData)




if __name__ == "__main__":
    main()
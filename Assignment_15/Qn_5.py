# Write a lambda function using reduce () which accepts a list of numbers and returns the maximum element

from functools import reduce

GetMax = lambda a,b: a if a > b else b


def main():
    Data = [10,55,23,59,34,22]
    print("Original Data is :",Data)


    RData = reduce(GetMax,Data)
    print("Max value is : ",RData)
    

if __name__ == "__main__":
    main()
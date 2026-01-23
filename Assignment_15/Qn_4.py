# Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements

from functools import reduce

Addition = lambda A,B : A + B

def main():
    Data = [10,20,30,40,50,60,70,80,90,100]
    print("The Actual Data is : ", Data)

    RData =reduce(Addition,Data)
    print("Addition of Data after reduce is : ", RData)

if __name__ == "__main__":
    main()

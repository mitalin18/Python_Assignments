# Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements

from functools import reduce

GetProduct = lambda no1, no2 : no1 * no2

def main():
    Data = [1,2,3,4,5,6,7,8,9,10]
    print("Original data is : ", Data)

    RData = reduce(GetProduct,Data)
    print("The product of elements is : ", RData)



if __name__ == "__main__":
    main()
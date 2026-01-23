# Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.



ChkOdd = lambda no: no % 2 !=0

def main():
    Data = [1,2,3,4,5,6,7,8,9,10]
    print("The Actual Data is : ", Data)

    FData = list(filter(ChkOdd,Data))
    print("Data after filter is : ",FData)

if __name__ == "__main__":
    main()
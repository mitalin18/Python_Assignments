# Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number

ListOfSq = lambda no: no * no

def main():
    Data = [2,3,4,5,6,7,8,9,10]
    print("Actual Data is : ", Data)

    MData = list(map(ListOfSq,Data))
    print("Data after map is : ",MData)

if __name__ == "__main__":
    main()
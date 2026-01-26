'''Write a program which accept N numbers from user and store it into List Return Minimum number from that List
Input Number of elements 4.
Input Elements 13 5 45 7
Output 5
'''

def getmin(elements):
    min_element = elements[0]
    for i in elements:
        if i < min_element:
            min_element = i
    return min_element

def main():
    NoOfElements = int(input("Enter the number of elements :"))
    Data = []

    print("Enter elements :")
    for i in range(NoOfElements):
        value = int(input())
        Data.append(value)

    result = getmin(Data)
    print("Minimum is : ",result)
  
if __name__ == "__main__":
    main()

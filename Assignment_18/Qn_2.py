'''Write a program which accept N numbers from user and store it into List Return Maximum number from that List
Input Number of elements 7
Input Elements 13 5 45 7 4 56 34
Output 56 '''

def getmax(elements):
    max_element = elements[0]
    for i in elements:
        if i > max_element:
            max_element = i
    return max_element

def main():
    NoOfElements = int(input("Enter the number of elements :"))
    Data = []

    print("Enter elements :")
    for i in range(NoOfElements):
        value = int(input())
        Data.append(value)

    result = getmax(Data)
    print("Max is : ",result)
  

if __name__ == "__main__":
    main()

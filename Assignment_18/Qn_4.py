'''Write a program which accept N numbers from user and store it into List Accept one another number from user and return 
frequency of that number from List.

Input Number of elements 11
Input Elements 13 5 45 7 4 56 5 34 2 5 65
Element to search 5
Output 3'''


def main():
    NoOfElements = int(input("Enter the number of elements :"))
    Data = []

    print("Enter elements :")
    for i in range(NoOfElements):
        value = int(input())
        Data.append(value)
    
    search_element = int(input("Enter the element to search :"))

    result = Data.count(search_element)
    print(result)

if __name__ == "__main__":
    main()


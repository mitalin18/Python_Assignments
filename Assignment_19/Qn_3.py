'''Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or 
equal to 70 and less than or equal to 90 Map function will increase each number by 10. Reduce will return product of all 
that numbers.

Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter (76, 89, 86, 90, 70]
Output of reduce
6538752000
List after map [86, 99, 96, 100, 80]
'''

from functools import reduce

def main():
    n = int(input("Enter number of elements: "))
    data = []

    print("Enter elements:")
    for i in range(n):
        data.append(int(input()))

    FData = list(filter(lambda x: x >= 70 and x <= 90, data))
    print("List after filter:", FData)

    MData = list(map(lambda x: x + 10, FData))
    print("List after map:", MData)

    result = reduce(lambda a, b: a * b, MData)
    print("Output of reduce:", result)

if __name__ == "__main__":
    main()

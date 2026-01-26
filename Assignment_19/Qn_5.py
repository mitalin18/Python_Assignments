'''Write a program which contains filter(), map() and reduce() in it Python application which contains one list of numbers 
List contains the numbers which are accepted from user Filter should filter out all prime numbers. 
Map function will multiply each number by 2 Reduce will return Maximum number from that numbers 
(You can also use normal functions instead of lambda functions)

Input List [2, 70, 11, 10, 17, 23, 31 771 
List after filter [2, 11, 17 23, 311 
List after map 14, 22, 34, 46, 621 
Output of reduce = 62'''


from functools import reduce

def is_prime(no):
    if no < 2:
        return False
    for i in range(2, int(no ** 0.5) + 1):
        if no % i == 0:
            return False
    return True

def main():
    print("Enter elements of list:")
    data = list(map(int, input().split()))

    FData = list(filter(is_prime, data))
    print("List after filter:", FData)

    MData = list(map(lambda x: x * 2, FData))
    print("List after map:", MData)

    result = reduce(lambda a, b: a if a > b else b, MData)
    print("Output of reduce:", result)

if __name__ == "__main__":
    main()

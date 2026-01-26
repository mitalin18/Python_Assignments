'''Write a program which contains one lambda function which accepts one parameter and return power of two.

Input 4
Output: 16

Input 6
Output: 64
'''

Power_Two = lambda no: 2 ** no

def main():
    no = int(input("Enter the number: "))
    result = Power_Two(no)
    print(result)

if __name__ == "__main__":
    main()
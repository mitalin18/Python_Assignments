'''Write a program which accept one number for user and check whether number is prime or not
Input
5
Output It is Prime Number
'''
def ChkPrime(no):

    if no <= 1:
        print("It is not a prime number")
        return
    
    for i in range(2, no):
        if no % i == 0:
            print("It is not a prime number")
            return 
    print("It is a prime number")
    
def main():
    no = int(input("Enter the number : "))
    ChkPrime(no)

if __name__ == "__main__":
    main()

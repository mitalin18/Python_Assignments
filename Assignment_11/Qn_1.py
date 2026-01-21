#1. Write a program which accepts one number and checks whether it is prime or not. Input: 11 Output: Prime Number

def ChkPrime(no):

    if no <= 1:
        print("Not prime")
        return
    
    for i in range(2, no):
        if no % i == 0:
            print("Not prime")
            return 
    print("Prime")
    
def main():
    no = int(input("Enter the number : "))
    ChkPrime(no)

if __name__ == "__main__":
    main()

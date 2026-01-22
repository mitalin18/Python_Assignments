# Write a lambda function which accepts two numbers and returns addition


Addition = lambda no1,no2: no1 + no2

def main():
    no1=  int(input("Enter first Number : "))
    no2 = int(input("Enter second Number : "))
    Result =  Addition(no1, no2)
    print(Result)
    

if __name__ == "__main__":
    main()
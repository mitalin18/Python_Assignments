'''Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() 
for multiplication and Div() for division. All functions accepts two parameters as number and perform the operation. 
Write on python program which call all the functions from Arithmetic module by accepting the parameters from user'''

def Add(No1,No2):
    res = No1 + No2
    print("Addition is : ",res)

def Sub(No1,No2):
    res = No1 - No2
    print("Subtraction is : ", res)

def Mul(No1,No2):
    res = No1 * No2
    print("Multiplication is ", res)

def Div(No1,No2):
    res = No1 /  No2
    print("Division is : ",res)


def main():
    No1= int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Add(No1,No2)
    Sub(No1,No2)
    Mul(No1,No2)
    Div(No1,No2)

if __name__ == "__main__":
    main()

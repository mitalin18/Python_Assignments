# Write a lambda function which accepts one number and returns square of that number.

def FindSq(no):
    Square = no * no
    print(Square)


FindSq = lambda no : no * no

def main():
    no = int(input("Enter the number : "))
    ret = FindSq(no)
    print("Square of number is : ", ret)

if __name__ == "__main__":
    main()

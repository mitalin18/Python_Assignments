# Write a lambda function which accepts one number and returns True if number is even otherwise False.

ChkEven = lambda no : True if no % 2 == 0 else False

def main():
    ret = False
    no = int(input("Enter the number : "))
    ret  = ChkEven(no)
    print(ret)
    

if __name__ == "__main__":
     main()

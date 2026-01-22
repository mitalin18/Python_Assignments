# Write a lambda function which accepts one number and returns True if number is odd otherwise False.

ChkOdd = lambda no : True if no % 2 != 0 else False

def main():
    ret = False
    no = int(input("Enter the number : "))
    ret  = ChkOdd(no)
    print(ret)
    

if __name__ == "__main__":
     main()

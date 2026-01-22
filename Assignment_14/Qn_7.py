# Write a lambda function which accepts one number and returns True if divisible by 5.

ChkDiv = lambda no : True if no % 5 == 0 else False

def main():
    ret = False
    no = int(input("Enter the number : "))
    ret  = ChkDiv(no)
    print(ret)
    

if __name__ == "__main__":
     main()

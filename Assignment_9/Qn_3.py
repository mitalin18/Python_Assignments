# Write a program which accepts one number and prints square of that number. Input: 5 Output: 25

def ChkSquare(no):

    res = no * no
    print("Square of the number",no, "is", res)
   

def main():

    no = int(input())
    ChkSquare(no)

if __name__ == "__main__":
    main()
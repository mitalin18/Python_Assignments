# Write a lambda function which accepts one number and returns cube of that number.


PrintCube = lambda no: no ** 3

def main():
    no = int(input("Enter the number : "))
    ret = PrintCube(no)
    print("Cube of the number is :", ret )

if __name__ == "__main__":
    main()

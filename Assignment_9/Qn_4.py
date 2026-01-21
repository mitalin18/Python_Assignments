# Write a program which accepts one number and prints cube of that number.

def ChkCube(no):
    result = no ** 3   # same as result = no * no * no

    print("The Cube of", no, "is", result)


def main():
    no = int(input())
    ChkCube(no)



if __name__ == "__main__":
    main()
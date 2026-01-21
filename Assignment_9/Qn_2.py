#Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.
#Input: 10 20
#Output: 20 is greater

def ChkGreater(no1, no2):

    if no1 > no2:
        print(no1, "Is greater")

    else:
        print(no2,"Is greater")


def main():
    ChkGreater(10, 20)

if __name__ == "__main__":
    main()

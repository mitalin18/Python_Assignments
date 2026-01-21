#5. Write a program which accepts one number and checks whether it is divisible by 3 and 5
#Input: 15
#Output: Divisible by 3 and 5


def ChkDivisible(no):
    if no % 3 == 0 & no % 5 ==0:
        print("Yes, it is divisible by 3 and 5")

    else:
        print("No, it is not divisible by 3 and 5")

def main():
    no = int(input())
    ChkDivisible(no)

if __name__ == "__main__":
    main()
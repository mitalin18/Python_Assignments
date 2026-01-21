# Write a program which accepts one number and prints binary equivalent.

def PrintBinary(no):
    binary_str = ""

    if no == 0:
        print("0")
        return 
    
    while no > 0:
        digit = no % 2
        binary_str = str(digit) + binary_str
        no= no // 2
    print(binary_str)


def main():
    no = int(input("Enter the number : "))
    PrintBinary(no)

if __name__ == "__main__":
    main()
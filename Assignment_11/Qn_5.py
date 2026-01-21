# Write a program which accepts one number and checks whether it is palindrome or not. Input: 121 Output: Palindrome

def ChkPalindrome(no):
    rev = 0
    original = no
    while no > 0:
        digit = no % 10
        rev = rev * 10 + digit
        no = no //10
    print(rev)
    if (rev == original):
        print("Palindrome")
    else:
        print("Not a Palindrome")


def main():
    no = int(input("Enyter the number : "))

    ChkPalindrome(no)


if __name__ == "__main__":
    main()

# Write a program which accepts one character and checks whether it is  vowel or consonant. Input: a Output: Vowel

def ChkVowel(alpha):
    #alpha = alpha.lower()
    if alpha.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")



def main():
    alpha = input("Enter the Character : ")
    ChkVowel(alpha)
    


if __name__ == "__main__":
    main()
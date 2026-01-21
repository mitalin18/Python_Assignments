''' 3. Write a program which accepts one number and prints factorial of that number. Input: 5 Output: 120  '''



def NumFact(no):
    Fact = 1
    for i in range(1, no + 1):    
        Fact = i * Fact

    print("Factorial is : ", Fact)

def main():
    no = int(input("Enter The number : "))
    NumFact(no)

if __name__ == "__main__":
    main()
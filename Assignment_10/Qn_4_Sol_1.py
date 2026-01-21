#  Write a program which accepts one number and prints all even numbers till that number Input: 10 Output: 2 4 6 8 10



def ShowEven(no):
    for i in range( 2, no +1, 2):
        print(i)
    
def main():
    no = int(input("Enter the number: "))
    ShowEven(no)

if __name__ == "__main__":
    main()



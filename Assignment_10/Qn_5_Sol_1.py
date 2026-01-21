#  Write a program which accepts one number and prints all odd numbers till that number 



def ShowEven(no):
    for i in range( 1, no +1, 2):
        print(i)
    
def main():
    no = int(input("Enter the number: "))
    ShowEven(no)

if __name__ == "__main__":
    main()



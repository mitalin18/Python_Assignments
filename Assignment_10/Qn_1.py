''' Write a program which accepts one number and prints multiplication table of that number.
Input: 4
Output:
4 8 12 16 20 24 28 32 36 40 '''

def MultTable(no):
    
    for i in range(1, 11):
        print(i * no)    # i = i * no
 
def main():
    no = int(input("Enter the number you want the table of : ")) 
    MultTable(no)

if __name__ == "__main__":
    main()
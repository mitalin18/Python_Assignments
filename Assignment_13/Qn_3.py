# Write a program which accepts one number and checks whether it is perfect number or not. Input: 6 Output: Perfect Number

def ChkPerfect(no):
    total = 0
    for i in range(1, no):
        if no % i == 0:
            total = total + i
        
    if total == no:
        print("Perfect Number")    

    else:
        print("Not a perfect number")

def main():
    no = int(input("Enter the number : "))
    ChkPerfect(no)

if __name__ == "__main__":
    main()
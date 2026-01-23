# Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.



ChkDiv = lambda no: no % 3 == 0 & no % 5 ==0

def main():
    Data = [12, 15, 135, 255, 25, 66, 10 ]
    print("Original Data is : ", Data)

    FData = list (filter(ChkDiv,Data))
    print("Nos divisible by both 3 and 5 are : ", FData)



if __name__ == "__main__":
    main()



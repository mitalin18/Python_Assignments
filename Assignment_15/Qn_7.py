# Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5


ChkLength = lambda str: len(str)> 5


def main():
    Data = ["Pune", "Mumbai","Jaipur", "Bengaluru","Delhi","Udaipur"]
    print("The original data is :", Data)

    FData = list(filter(ChkLength,Data))
    print("list of string having length > 5 is : ",FData)


if __name__ == "__main__":
    main()
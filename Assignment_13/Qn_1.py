# Write a program which accepts length and width of rectangle and prints area.

def RectArea(length , width):
    Area = 0
    Area = length * width
    print("The Area is : ", Area)


def main():
    length = int(input("Enter the length : "))
    width = int(input("Enter the width : "))
    RectArea(length , width)

if __name__ == "__main__":
    main()
# Write a program which accepts radius of circle and prints area of circle.

def CircleArea(radius):
    Area = 0
    pi = 3.14
    Area = pi * radius ** 2
    print("The Area of Circle is : ", Area)

def main():
    radius = int(input("Enter the radius : "))
    CircleArea(radius)

if __name__ == "__main__":
    main()

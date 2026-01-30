'''Write a Python program to implement a class named Numbers with the following specifications:
The class should contain one instance variable:
Value
Define a constructor (init) that accepts a number from the user and initializes Value
Implement the following instance methods:
ChkPrime()- returns True if the number is prime, otherwise returns False
ChkPerfect()returns True if the number is perfect otherwise returns False
Factors()-displays all factors of the number
SumFactors()returns the sum of all factors
(You may use this method as a helper in ChkPerfect() if required)
Create multiple objects and call all methods.'''


class Numbers:
    def __init__(self, no):
        self.Value = no

    def ChkPrime(self):
        if self.Value < 2:
            return False
        for i in range(2, int(self.Value / 2) + 1):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print("Factors of", self.Value, ":")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total

    def ChkPerfect(self):
        return self.SumFactors() == self.Value


def main():
    num1 = Numbers(6)
    print("Number:", num1.Value)
    print("Is Prime:", num1.ChkPrime())
    num1.Factors()
    print("Sum of factors:", num1.SumFactors())
    print("Is Perfect:", num1.ChkPerfect())
    print("-------------------------")

    num2 = Numbers(7)
    print("Number:", num2.Value)
    print("Is Prime:", num2.ChkPrime())
    num2.Factors()
    print("Sum of factors:", num2.SumFactors())
    print("Is Perfect:", num2.ChkPerfect())


if __name__ == "__main__":
    main()

'''Write a Python program to implement a class named BankAccount with the following requirements:
The class should contain two instance variables:
Name (Account holder name)
Amount (Account balance)
The class should contain one class variable
ROI (Rate of Interest), initialized to 10.5
Define a constructor ( init ) that accepts Name and initial Amount
Implement the following instance methods:
Display()displays account holder name and current balance
Deposit()-accepts an amount from the user and adds it to balance
Withdraw() accepts an amount from the user and subtracts it from balance Ensure withdrawat is allowed only if sufficient balance exists)
CalculateInterest() calculates and returns interest using formula
Interest (Amount ROI) / 100
Create multiple objects and demonstrate all methods'''


class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder Name:", self.Name)
        print("Account Balance:", self.Amount)

    def Deposit(self):
        deposit_amount = float(input("Enter amount to deposit: "))
        self.Amount += deposit_amount
        print("Amount deposited successfully")

    def Withdraw(self):
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount <= self.Amount:
            self.Amount -= withdraw_amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


def main():
    acc1 = BankAccount("Amit", 10000)
    acc1.Display()
    acc1.Deposit()
    acc1.Withdraw()
    print("Interest:", acc1.CalculateInterest())
    acc1.Display()
    print("---------------------------")

    acc2 = BankAccount("Sneha", 5000)
    acc2.Display()
    acc2.Deposit()
    acc2.Withdraw()
    print("Interest:", acc2.CalculateInterest())
    acc2.Display()


if __name__ == "__main__":
    main()

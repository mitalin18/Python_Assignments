'''Design a Python application that creates two threads named EvenList and OddList.
Both threads should accept a list of integers as input.
The EvenList thread should:
-Extract all even elements from the list.
-Calculate and display their sum

The OddList thread should:
-Extract all odd elements from the list.
-Calculate and display their sum

Threads should run concurrently'''

import threading

def EvenList(numbers):
    even_nums = []
    total = 0
    for no in numbers:
        if no % 2 == 0:
            even_nums.append(no)
            total += no
    print("Even numbers:", even_nums)
    print("Sum of even numbers:", total)


def OddList(numbers):
    odd_nums = []
    total = 0
    for no in numbers:
        if no % 2 != 0:
            odd_nums.append(no)
            total += no
    print("Odd numbers:", odd_nums)
    print("Sum of odd numbers:", total)


def main():
    print("Enter elements of list:")
    data = list(map(int, input().split()))

    t1 = threading.Thread(target=EvenList, args=(data,), name="EvenList")
    t2 = threading.Thread(target=OddList, args=(data,), name="OddList")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()

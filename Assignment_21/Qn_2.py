'''Design a Python application that creates two threads.
Thread I should calculate and display the maximum element from an list
Thread 2 should calculate and display the minimum element from the same list
The list should be accepted from the user
'''

import threading

def find_max(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    print("Maximum element:", max_val)


def find_min(numbers):
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    print("Minimum element:", min_val)


def main():
    print("Enter elements of list:")
    data = list(map(int, input().split()))

    t1 = threading.Thread(target=find_max, args=(data,), name="MaxThread")
    t2 = threading.Thread(target=find_min, args=(data,), name="MinThread")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()

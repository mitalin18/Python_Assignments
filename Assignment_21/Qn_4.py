'''Design a Python application that creates two threads.
Thread I should compute the sum of elements from a list
Thread 2 should compute the product of elements from the same list
Return the results to the main thread and display them'''

import threading

sum_result = 0
product_result = 1

def calculate_sum(numbers):
    global sum_result
    total = 0
    for num in numbers:
        total += num
    sum_result = total


def calculate_product(numbers):
    global product_result
    prod = 1
    for num in numbers:
        prod *= num
    product_result = prod


def main():
    print("Enter elements of list:")
    data = list(map(int, input().split()))

    t1 = threading.Thread(target=calculate_sum, args=(data,), name="SumThread")
    t2 = threading.Thread(target=calculate_product, args=(data,), name="ProductThread")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements:", sum_result)
    print("Product of elements:", product_result)
    print("Exit from main")


if __name__ == "__main__":
    main()

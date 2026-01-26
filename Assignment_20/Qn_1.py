'''Design a Python application that creates two separate threads named Even and Odd.
The Even thread should display the first 10 even numbers.
The Odd thread should display the first 10 odd numbers
Both threads should execute independently using the threading module.
Ensure proper thread creation and execution
'''

import threading

def print_even():
    print("Even Thread:")
    for i in range(1, 11):
        print(i * 2)

def print_odd():
    print("Odd Thread:")
    for i in range(10):
        print(2 * i + 1)

def main():
    even_thread = threading.Thread(target=print_even, name="Even")
    odd_thread = threading.Thread(target=print_odd, name="Odd")

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Both threads have finished execution.")

if __name__ == "__main__":
    main()

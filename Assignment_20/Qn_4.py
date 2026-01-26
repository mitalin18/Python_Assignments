'''Design a Python application that creates three threads named Small, Capital, and Digits.
All threads should accept a string as input
The Small thread should count and display the number of lowercase characters.
The Capital thread should count and display the number of uppercase characters
The Digits thread should count and display the number of numeric digits.
Each thread must also display
Thread ID
Thread Name'''

import threading

def Small(text):
    count = 0
    for ch in text:
        if ch.islower():
            count += 1
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())
    print("Lowercase count:", count)
    print()


def Capital(text):
    count = 0
    for ch in text:
        if ch.isupper():
            count += 1
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())
    print("Uppercase count:", count)
    print()


def Digits(text):
    count = 0
    for ch in text:
        if ch.isdigit():
            count += 1
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID:", threading.get_ident())
    print("Digit count:", count)
    print()


def main():
    data = input("Enter a string: ")

    t1 = threading.Thread(target=Small, args=(data,), name="Small")
    t2 = threading.Thread(target=Capital, args=(data,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(data,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")


if __name__ == "__main__":
    main()

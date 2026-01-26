'''Design a Python application that creates two threads named Thread1 and Thread2.
Thread1 should display numbers from 1 to 50.
Thread2 should display numbers from 50 to 1 in reverse order
Ensure that Thread2 starts execution only after Thread1 has completed.
Use appropriate thread synchromzation'''

import threading

def display_forward():
    print("Thread1 started")
    for i in range(1, 51):
        print(i)
    print("Thread1 completed\n")


def display_reverse():
    print("Thread2 started")
    for i in range(50, 0, -1):
        print(i)
    print("Thread2 completed")


def main():
    t1 = threading.Thread(target=display_forward, name="Thread1")
    t2 = threading.Thread(target=display_reverse, name="Thread2")

    
    t1.start()

    t1.join()

    t2.start()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()

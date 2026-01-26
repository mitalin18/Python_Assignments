'''Design a Python application where multiple threads update a shared variable
Use a Lock to avoid race conditions.
Each thread should increment the shared counter multiple times
Display the final value of the counter after all threads complete execution.'''

import threading

counter = 0

lock = threading.Lock()

def increment_counter():
    global counter
    for i in range(1000):            
        lock.acquire()
        counter += 1
        lock.release()

def main():
    threads = []

    for i in range(5):               
        t = threading.Thread(target=increment_counter)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Final value of counter:", counter)

if __name__ == "__main__":
    main()

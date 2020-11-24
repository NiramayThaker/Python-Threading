import _thread
import time


def Work(name, delay):
    count = 0

    while count < 5:
        time.sleep(delay)

        count += 1

        print("{} {}".format(name, count))


def Main():
    i = 0

    while i < 10:
        print("Loop 1")

        i += 1

    _thread.start_new_thread(Work, ("Jagrat", 0.5))

    _thread.start_new_thread(Work, ("Amit", 0.2))

    i = 0

    while i < 10:
        print("Loop 2")

        time.sleep(0.2)

        i += 1


Main()
time.sleep(5)

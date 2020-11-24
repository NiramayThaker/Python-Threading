import _thread
import threading
import time


class Thread1(threading.Thread):

    def __init__(self, name, delay):
        threading.Thread.__init__(self)

        self.name = name

        self.delay = delay

    def run(self):
        count = 0

        while count < 5:
            time.sleep(self.delay)

            count += 1

            print("{} {}".format(self.name, count))


def Main():
    print("Entering Main")

    i = 0

    while i < 10:
        print("Loop 1")

        i += 1

    t1 = Thread1("Amit", 0.6)

    t1.start()

    i = 0

    while i < 10:
        print("Main")

        time.sleep(0.5)

        i += 1

    print("Leaving Main")


Main()

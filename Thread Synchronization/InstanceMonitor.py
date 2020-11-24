from threading import *

import time


class RacingCircuit:

    def __init__(self):

        self.lap = 0

        self.monitor = Condition()

    def busyTracks(self):

        with self.monitor:

            t = current_thread()

            print("{} Entered Busy Tracks".format(t.name))

            while (self.lap < 5):

                if (t.name == "Car"):
                    print("brrrommsss")

                else:
                    print("vrrrommsss")

                time.sleep(1)

                self.lap += 1

                print("Lap = {}".format(self.lap))

            self.lap = 0

            print("{} Leaving Busy Tracks".format(t.name))

    def busyLanes(self):

        with self.monitor:

            t = current_thread()

            print("{} Entered Busy Lanes".format(t.name))

            while (self.lap < 5):

                if (t.name == "Car"):
                    print("brrrommsss")

                else:
                    print("vrrrommsss")

                time.sleep(1)

                self.lap += 1

                print("Lap = {}".format(self.lap))

            self.lap = 0

            print("{} Leaving Busy Tracks".format(t.name))


a = RacingCircuit()

b = RacingCircuit()


class Bike(Thread):

    def __init__(self):
        Thread.__init__(self, name="Bike")

    def run(self):
        print("Bike Starts Journey")

        global a

        global b

        a.busyTracks()

        a.busyLanes()

        b.busyLanes()

        a.busyTracks()

        print("Bike Ends Journey")


class Car(Thread):

    def __init__(self):
        Thread.__init__(self, name="Car")

    def run(self):
        print("Car Starts Journey")

        global b

        global a

        b.busyLanes()

        b.busyTracks()

        b.busyLanes()

        a.busyTracks()

        print("Car Ends Journey")


Car().start()

Bike().start()

import time
import threading


def upper_tri():
	for i in range(0, 5):

		for k in range(0, 5 - i):
			print('', end=' ')

		for j in range(0, i):
			print('*', end=' ')

		print()


def lower_tri():
	for i in range(5, 0, -1):

		for k in range(5 - i, 0, -1):
			print(' ', end='')

		for j in range(0, i):
			print('*', end=' ')

		print()


t1 = threading.Thread(target=upper_tri)
t2 = threading.Thread(target=lower_tri)

t1.start()
time.sleep(0.2)
t2.start()
time.sleep(0.2)


t1.join()
t2.join()


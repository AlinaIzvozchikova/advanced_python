"""
Task - modified output numbers in order.

First thread put numbers from 0..100 to shared number list
with random time sleeps.
Second thread listen number list, if there are even numbers
print it and remove from list.
Third thread listen number list, if there are odd numbers
print it and remove from list.
Added shared number list outputs for show it filling.

Using Semaphore synchronization object.
"""
import random
import time

from threading import Semaphore
from threading import Thread


MAX_NUMBER_LIST = 100


def number_list_writer(number_list):
    """Put element to number list from range with sleep.

    :param number_list: shared number list

    """
    for i in range(0, MAX_NUMBER_LIST + 1):
        number_list.append(i)
        time.sleep(random.uniform(0.01, 0.1))


def even_numbers_reader(thread_max_print_count,
                        even_thread_semaphore,
                        odd_thread_semaphore,
                        number_list):
    """Listen shared number list, if there are even numbers
    print it and remove from list.

    :param thread_max_print_count: max count of print
    :param even_thread_semaphore: even lock
    :param odd_thread_semaphore: odd lock
    :param number_list: shared number list

    """
    max_print_count = 0
    while max_print_count < thread_max_print_count:
        if number_list and number_list[0] % 2 == 0:
            even_thread_semaphore.acquire()
            print(number_list[0], number_list)
            number_list.remove(number_list[0])
            max_print_count += 1
            odd_thread_semaphore.release()
        else:
            time.sleep(0.1)


def odd_numbers_reader(thread_max_print_count,
                       even_thread_semaphore,
                       odd_thread_semaphore,
                       number_list):
    """Listen shared number list, if there are odd numbers
    print it and remove from list.

    :param thread_max_print_count: max count of print
    :param even_thread_semaphore: even lock
    :param odd_thread_semaphore: odd lock
    :param number_list: shared number list

    """
    max_print_count = 0
    while max_print_count < thread_max_print_count:
        if number_list and number_list[0] % 2 != 0:
            odd_thread_semaphore.acquire()
            print(number_list[0], number_list)
            number_list.remove(number_list[0])
            max_print_count += 1
            even_thread_semaphore.release()
        else:
            time.sleep(0.1)


if __name__ == '__main__':

    number_list = []

    even_thread_max_print_count = int(MAX_NUMBER_LIST / 2 + 1)
    odd_thread_max_print_count = int(MAX_NUMBER_LIST / 2)

    max_connections = 1

    even_thread_semaphore = Semaphore(1)
    odd_thread_semaphore = Semaphore(0)

    writer_thread = Thread(
        target=number_list_writer,
        args=(number_list, )
    )
    reader_even_thread = Thread(
        target=even_numbers_reader,
        args=(even_thread_max_print_count,
              even_thread_semaphore,
              odd_thread_semaphore,
              number_list)
    )
    reader_odd_thread = Thread(
        target=odd_numbers_reader,
        args=(odd_thread_max_print_count,
              even_thread_semaphore,
              odd_thread_semaphore,
              number_list)
    )

    writer_thread.start()
    reader_even_thread.start()
    reader_odd_thread.start()

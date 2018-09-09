"""
Task - Output numbers from 0..100 in order.
First process loop number list, if there are even numbers
print it.
Second thread loop number list, if there are odd numbers
print it.

Using Lock synchronization object and shared memory.
"""
from multiprocessing import Process, Array, Lock

MAX_NUMBER_LIST = 100


def even_numbers_reader(number_list,
                        lock_p_even,
                        lock_p_odd):
    """Loop number list, if there are even numbers print it.

    :param lock_p_even: even lock
    :param lock_p_odd: odd lock
    :param number_list: number list
    :return:
    """
    for number in number_list:
        if number % 2 == 0:
            lock_p_odd.acquire()
            print(number)
            lock_p_even.release()


def odd_numbers_reader(number_list,
                       lock_p_even,
                       lock_p_odd):
    """Loop number list, if there are odd numbers print it.

    :param lock_p_even: even lock
    :param lock_p_odd: odd lock
    :param number_list: number list
    :return:
    """
    for number in number_list:
        if number % 2 != 0:
            lock_p_even.acquire()
            print(number)
            lock_p_odd.release()


if __name__ == '__main__':

    number_list = Array('i', range(0, MAX_NUMBER_LIST + 1))

    lock_p_even = Lock()
    lock_p_odd = Lock()
    
    lock_p_even.acquire()

    p_even = Process(target=even_numbers_reader,
                     args=(number_list,
                           lock_p_even,
                           lock_p_odd))

    p_odd = Process(target=odd_numbers_reader,
                    args=(number_list,
                          lock_p_even,
                          lock_p_odd))

    p_even.start()
    p_odd.start()

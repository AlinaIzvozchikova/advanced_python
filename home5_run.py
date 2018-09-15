"""
    Homework for Advanced Python course.
    Output sum of prime numbers in the specified range [n, m].
    Use concurrent.futures or/and asyncio.
"""

import asyncio


async def get_prime(number):
    """Get value of number if it is prime else return 0

    :param number: number
    :return: number if it is prime else return 0

    """

    is_prime = True
    for i in range(1, int((number + (number % 2)) / 2)):
        i += 1
        if (number % i) == 0:
            is_prime = False
            break
    if is_prime:
        print(str(number) + ' prime')
        return number
    return 0


async def get_prime_sum(start, finish):
    """Get sum of prime numbers from range.

    :param start: start range from
    :param finish: finish range to
    :return: sum of prime numbers

    """

    prime_sum = 0

    for i in range(start, finish + 1):
        if i == 1:
            continue
        prime_sum += await get_prime(i)

    return prime_sum


if __name__ == '__main__':

    start_from = 1
    finish_to = 100

    if start_from > finish_to:
        raise ResourceWarning('start_from less then finish_to param')

    event_loop = asyncio.get_event_loop()

    sum_result = event_loop.run_until_complete(get_prime_sum(start_from,
                                                             finish_to))
    print('Sum of prime: {} from ({}, {}) '
          .format(sum_result, start_from, finish_to))

    event_loop.close()

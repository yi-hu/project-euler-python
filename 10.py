from itertools import takewhile
from math import sqrt
import timeit


def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def primes():
    yield 2
    yield 3
    i = 6
    while True:
        if is_prime(i - 1):
            yield i - 1
        if is_prime(i + 1):
            yield i + 1
        i += 6


def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(sqrt(n)) + 1):
        if not sieve[i]:
            continue
        else:
            for j in range(2, int(n / i) + 1):
                sieve[i * j] = False
    return [i for i in range(len(sieve)) if sieve[i]]


if __name__ == "__main__":
    start_time = timeit.default_timer()
    answer = sum(takewhile(lambda x: x < 2 * 10 ** 6, primes()))
    elapsed = timeit.default_timer() - start_time
    print("Problem 10 (slow method):", answer)
    print("Time elapsed: {}".format(elapsed))

    start_time = timeit.default_timer()
    answer = sum(sieve_of_eratosthenes(2 * 10 ** 6))
    elapsed = timeit.default_timer() - start_time
    print("Problem 10 (Sieve of Eratosthenese):", answer)
    print("Time elapsed: {}".format(elapsed))

from itertools import count
from itertools import takewhile
import timeit


def max_prime_factor(n):
    if is_prime(n):
        return n
    min_prime = min_prime_factor(n)
    return max(min_prime, max_prime_factor(n // min_prime))


def min_prime_factor(small_n):
    for p in takewhile(lambda x: x <= small_n, primes()):
        if small_n % p == 0:
            return p


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
    for i in count(6, 6):
        if is_prime(i - 1):
            yield i - 1
        if is_prime(i + 1):
            yield i + 1


if __name__ == "__main__":
    start_time = timeit.default_timer()
    answer = max_prime_factor(600851475143)
    elapsed = timeit.default_timer() - start_time
    print("Problem 3:", answer)
    print("Time elapsed: {}".format(elapsed))

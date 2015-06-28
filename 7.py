from itertools import count


def primes():
    yield 2
    yield 3
    for i in count(6, 6):
        if is_prime(i - 1):
            yield i - 1
        if is_prime(i + 1):
            yield i + 1


def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


if __name__ == "__main__":
    prime_iter = primes()
    for _ in range(10001):
        answer = next(prime_iter)
    print("Problem 7:", answer)

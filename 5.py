from functools import reduce


def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def min_prime_factors(n):
    if n == 1:
        return [1]
    prev = min_prime_factors(n - 1)
    if is_prime(n):
        return prev + [n]
    else:
        return prev + [find_missing_prime_factor(n, prev)]


def find_missing_prime_factor(n, factors):
    for i in factors:
        if n % i == 0:
            n = n // i
    return n


if __name__ == "__main__":
    factors = min_prime_factors(20)
    answer = reduce(lambda x, y: x * y, factors, 1)
    print("Problem 5:", answer)

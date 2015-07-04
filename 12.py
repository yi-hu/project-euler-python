from functools import reduce


def triangular_numbers():
    n = 1
    while True:
        yield n * (n + 1) // 2
        n += 1


def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if not sieve[i]:
            continue
        else:
            for j in range(2, int(n / i) + 1):
                sieve[i * j] = False
    return [i for i in range(len(sieve)) if sieve[i]]


# can be further optimize of we cache the prime numbers
def find_prime_factors(n):
    if n == 1:
        return {}
    result = {}
    primes = sieve_of_eratosthenes(int(n ** 0.5) + 1)
    for p in primes:
        while n % p == 0:
            n = n // p
            result[p] = result.get(p, 0) + 1
    if n > 1:
        result[n] = 1
    return result


def count_factors(n):
    if n == 1:
        return 1
    if is_prime(n):
        return 2
    prime_factors = find_prime_factors(n)
    return reduce(lambda x, y: x * y, (v + 1 for k, v in prime_factors.items()))

if __name__ == "__main__":
    t = triangular_numbers()
    n = next(t)
    while count_factors(n) <= 500:
        n = next(t)
    answer = n
    print("Problem 12:", answer)

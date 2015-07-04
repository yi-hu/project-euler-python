from itertools import count


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


def find_prime_factors_cached(prime_limit):
    primes = sieve_of_eratosthenes(prime_limit)

    def prime_factors(n):
        result = set()
        if n > prime_limit ** 2:
            return result
        for p in primes:
            while n % p == 0:
                n = n // p
                result.add(p)
        if n > 1:
            result.add(n)
        return result
    return prime_factors


if __name__ == "__main__":
    find_prime_factors = find_prime_factors_cached(10 ** 4)
    prime_factor_count = {}
    while True:
        for i in count(2, 1):
            for j in range(4):
                if i + j not in prime_factor_count.keys():
                    prime_factor_count[i + j] = len(find_prime_factors(i + j))
            if prime_factor_count[i] == 0:
                break
            if 4 == prime_factor_count[i] == prime_factor_count[i + 1] == prime_factor_count[i + 2] == prime_factor_count[i + 3]:
                break
        break
    print(i)

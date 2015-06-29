import timeit


def time_function(f):
    def wrapper_f(*args, **kwargs):
        print(f.__name__ + "{}{} is being called...".format(args, kwargs))
        start_time = timeit.default_timer()
        result = f(*args, **kwargs)
        elapsed = timeit.default_timer() - start_time
        print(f.__name__ + "{}{} has ended in {}".format(args, kwargs, elapsed))
        return result
    return wrapper_f


@time_function
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


def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def is_circular_prime(prime):
    prime = str(prime)
    for i in range(len(prime) - 1):
        prime = prime[-1] + prime[:-1]
        if not is_prime(int(prime)):
            return False
    return True


if __name__ == "__main__":
    primes = sieve_of_eratosthenes(10 ** 6)
    answer = sum(1 for p in primes if is_circular_prime(p))
    print("Problem 35:", answer)

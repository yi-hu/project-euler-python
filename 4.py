import timeit


def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    start_time = timeit.default_timer()
    answer = max((x * y, x, y) for x in range(1000)
                 for y in range(1000)
                 if is_palindrome(x * y))
    elapsed = timeit.default_timer() - start_time
    print("Problem 4:", answer)
    print("Time elapsed: {}".format(elapsed))

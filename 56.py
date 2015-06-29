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


def sum_digits(number):
    number = str(number)
    return sum(map(lambda i: int(i), number))


@time_function
def find_max_sum_digits(n):
    return max(sum_digits(a ** b)
               for a in range(1, n)
               for b in range(1, n))


if __name__ == "__main__":
    answer = find_max_sum_digits(100)
    print("Problem 56:", answer)

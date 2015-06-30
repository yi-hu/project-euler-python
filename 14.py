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


def count_collatz_chain(n):
    count = 1
    while n >= 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        count += 1
    return count


@time_function
def build_collatz_chain_steps_lookup(n):
    result = [0] * n
    result[1] = 1
    for i in range(2, n):
        fill_lookup(i, result)
    return result


def fill_lookup(i, lookup_array):
    if lookup_array[i] == 0:
        count = 1
        j = i
        while True:
            j = j // 2 if j % 2 == 0 else 3 * j + 1
            if j < len(lookup_array):
                fill_lookup(j, lookup_array)
                lookup_array[i] = count + lookup_array[j]
                break
            count += 1


if __name__ == "__main__":
    chain_steps_count = build_collatz_chain_steps_lookup(10 ** 6)
    answer = chain_steps_count.index(max(chain_steps_count))
    print("Problem 14:", answer)

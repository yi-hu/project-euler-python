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




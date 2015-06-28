from itertools import takewhile


def fib():
    a, b = 1, 1
    while True:
        yield b
        a, b = b, a + b

if __name__ == "__main__":
    fib_numbers = takewhile(lambda x: x < 4 * 10 ** 6, fib())
    answer = sum(i for i in fib_numbers if i % 2 == 0)
    print("Problem 2:", answer)

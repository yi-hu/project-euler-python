def fib():
    a, b = 1, 1
    while True:
        yield b
        a, b = b, a + b


if __name__ == "__main__":
    i = 1
    num = 1
    fib_squence = fib()
    while len(str(num)) < 1000:
        num = next(fib_squence)
        i += 1
    answer = i
    print("Problem 25:", answer)

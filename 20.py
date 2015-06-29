from math import factorial


def sum_digits(number):
    number = str(number)
    return sum(map(lambda i: int(i), number))


if __name__ == "__main__":
    answer = sum_digits(factorial(100))
    print("Problem 20", answer)

def is_sum_of_powers_of_digits(number, pow):
    return int(number) == sum(map(lambda i: int(i) ** pow, str(number)))


if __name__ == "__main__":
    answer = [i for i in range(2, 5 * 9 ** 5) if is_sum_of_powers_of_digits(i, 5)]
    print(answer)
    answer = sum(answer)
    print("Problem 30:", answer)

if __name__ == "__main__":
    answer = sum(range(1, 101)) ** 2 - sum(map(lambda x: x ** 2, range(1, 101)))
    print("Problem 6:", answer)

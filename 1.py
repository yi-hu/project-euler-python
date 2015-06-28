if __name__ == "__main__":
    answer = sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)
    print("Problem 1:", answer)

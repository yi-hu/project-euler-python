

if __name__ == "__main__":
    answer = sum(i ** i for i in range(1, 1001))
    answer = str(answer)[-10: ]
    print("Problem 48:", answer)

if __name__ == "__main__":
    answer = [(a * b * (1000 - a - b), a, b, 1000 - a - b)
              for a in range(1, 1000)
              for b in range(1, a + 1)
              if a ** 2 + b ** 2 == (1000 - a - b) ** 2]
    print("Problem 9:", answer)

import pandas as pd
from pprint import pprint as pp
from functools import reduce


if __name__ == "__main__":
    data = pd.read_csv("data/11.txt", delim_whitespace=True, header=None)
    product = lambda x, y: x * y
    m, n = data.shape
    max_horizontal_product = max((reduce(product, data.iloc[i, j:j + 4]), i, j)
                                 for i in range(m)
                                 for j in range(n)
                                 if j + 4 <= n)
    max_vertical_product = max((reduce(product, data.iloc[i:i + 4, j]), i, j)
                                 for i in range(m)
                                 for j in range(n)
                                 if i + 4 <= m)
    max_diagonal_product_l2r = max((reduce(product, (data.iloc[i + k, j + k] for k in range(4))), i, j)
                                 for i in range(m) if i + 4 <= m
                                 for j in range(n) if j + 4 <= n)
    max_diagonal_product_r2l = max((reduce(product, (data.iloc[i + k, j - k] for k in range(4))), i, j)
                                 for i in range(m) if i + 4 <= m
                                 for j in range(n)
                                 if j - 4 >= 0)
    answer = max(max_horizontal_product, max_vertical_product,
                 max_diagonal_product_l2r, max_diagonal_product_r2l)
    print("Project 11:", answer)

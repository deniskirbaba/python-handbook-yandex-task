import numpy as np
import pandas as pd


def values(func, start, end, step):
    n = int(abs((end - start) / step)) + 1
    x = np.linspace(start, end, num=n)
    return pd.Series(data=[func(i) for i in x], index=x)


def min_extremum(data: pd.Series):
    return data.idxmin()


def max_extremum(data: pd.Series):
    return data.idxmax()


# Tests for values func
print(values(lambda x: x ** 2 + 2 * x + 1, -1.5, 1.7, 0.1))
print(values(lambda x: x ** 2 + 2 * x + 1, -1.5, 1.7, 2))
print(values(lambda x: x ** 2 + 2 * x + 1, -1.5, 4.5, 2))

# data = values(lambda x: x ** 2 + 2 * x + 1, -1.5, 1.7, 0.1)
# print(data)
# print(min_extremum(data))
# print(max_extremum(data))

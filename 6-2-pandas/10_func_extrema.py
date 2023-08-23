import numpy as np
import pandas as pd


def arange(start, stop, step=1, endpoint=True):
    arr = np.arange(start, stop, step)
    if endpoint and np.isclose(arr[-1] + step, stop):
        arr = np.concatenate([arr, [arr[-1] + step]])

    return arr


def values(func, start, end, step):
    x = arange(start, end, step, endpoint=True)
    return pd.Series(data=[func(i) for i in x], index=x)


def min_extremum(data: pd.Series):
    return data.idxmin()


def max_extremum(data: pd.Series):
    return data.idxmax()


data = values(lambda x: x ** 2 + 2 * x + 1, -1.5, 1.7, 0.1)
print(data)
print(min_extremum(data))
print(max_extremum(data))

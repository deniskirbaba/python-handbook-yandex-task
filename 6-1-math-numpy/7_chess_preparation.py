import numpy as np


def make_board(n):
    res = np.zeros(shape=(n, n), dtype=np.int8)
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                res[i, j] = 1 
    return res


print(make_board(4))

import numpy as np


def snake(m, n, direction='H'):
    res = np.zeros(shape=(n, m), dtype=np.int16)
    cur_n = 1
    if direction == 'V':
        for j in range(m):
            for i in range(n):
                if j % 2 == 1:
                    res[n - i - 1, j] = cur_n
                else:
                    res[i, j] = cur_n
                cur_n += 1
    else:
        for i in range(n):
            for j in range(m):
                if i % 2 == 1:
                    res[i, m - j - 1] = cur_n
                else:
                    res[i, j] = cur_n
                cur_n += 1
    return res


print(snake(5, 3, direction='V'))

import numpy as np


def stairs(v):
    res = np.zeros(shape=(len(v), len(v)), dtype=v.dtype)
    for i in range(len(v)):
        res[i] = np.concatenate((v[-i:], v[:-i]))
    return res


print(stairs(np.arange(3)))
print(stairs(np.arange(5)))


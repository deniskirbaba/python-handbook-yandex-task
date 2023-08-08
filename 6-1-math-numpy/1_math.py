import numpy as np
import math


x = float(input())
res = math.log(x ** (3 / 16), 32) + np.power(x, np.cos(np.pi * x / (2 * np.e))) - np.power(np.sin(x / np.pi), 2)
print(res)
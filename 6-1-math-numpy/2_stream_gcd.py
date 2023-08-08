import numpy as np
import math
from sys import stdin


res = []
for seq in stdin:
    res.append(math.gcd(*map(int, seq.split())))
[print(i) for i in res]

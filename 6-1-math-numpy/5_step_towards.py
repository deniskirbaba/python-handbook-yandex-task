import numpy as np
from math import dist


cart_deca = np.array([float(i) for i in input().split()])
polar_pola = np.array([float(i) for i in input().split()])
cart_pola = np.array([np.cos(polar_pola[1]), np.sin(polar_pola[1])]) * polar_pola[0]
d = dist(cart_pola, cart_deca)
print(d)

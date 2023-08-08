import numpy as np


def rotate(mat, deg):
    match deg:
        case 90:
            return np.rot90(mat, -1)
        case 180:
            return np.rot90(mat, -2)
        case 270:
            return np.rot90(mat, -3)
        case _:
            return mat
        

#print(rotate(np.arange(12).reshape(3, 4), 90))
print(rotate(np.arange(12).reshape(3, 4), 270))

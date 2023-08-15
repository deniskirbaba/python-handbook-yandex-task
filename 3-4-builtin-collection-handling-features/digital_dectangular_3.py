from itertools import product

height = int(input())
width = int(input())

len_col = len(str(height * width))

width_values = range(1, width + 1)
height_values = range(1, height + 1)

[print(' '.join([str((h - 1) * width + w).rjust(len_col) for h, w in product([h_i], width_values)]))
 for h_i in height_values]

rle = [('1', 1), ('0', 2), ('5', 1), ('0', 2)]

s = ''.join([i * n for (i, n) in rle])

print(s)

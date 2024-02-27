# size = int(input())

# square = [[1 for i in range(size)] for i in range(size)]

# times = size / 2 - 1

# for i in range(1, int(times) + 1):
#     for j in range(i, size - i):
#         for k in range(i, size - i):
#             square[j][k] += 1

# if times % 1 != 0:
#     square[size // 2][size // 2] += 1

# max_n = (size + 1) // 2

# for i in square:
#     print(' '.join([f'{j: >{len(str(max_n))}}' for j in i]))

for i in range(n := int(input())):
    for j in range(n):
        d = str(min(i, j, n - i - 1, n - j - 1) + 1)
        print(d.rjust(len(str((n + 1) // 2)), ' '), end=' ' if j < n - 1 else '\n')
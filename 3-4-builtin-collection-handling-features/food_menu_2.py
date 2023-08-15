from itertools import cycle

n_porridges = int(input())
porridges = [input() for i in range(n_porridges)]
n_days = int(input())

cur_day = 0
for i in cycle(porridges):
    if cur_day < n_days:
        print(i)
    else:
        break
    cur_day += 1

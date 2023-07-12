from itertools import count

start, stop, step = [float(i) for i in input().split()]

for i in count(start, step):
    if i <= stop:
        print(i)
    else:
        break

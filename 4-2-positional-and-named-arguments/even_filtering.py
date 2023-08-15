print(*filter(lambda n: sum((int(i) for i in str(n))) % 2 == 0, (32, 64, 128, 256, 512)))

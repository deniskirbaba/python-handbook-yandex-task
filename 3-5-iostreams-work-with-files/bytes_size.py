import os
from math import ceil

filename = input()
path = '3-5-iostreams-work-with-files/data'

stat_info = os.stat(os.path.join(path, filename))
units = ['б', 'Б', 'КБ', 'МБ', 'ГБ']
size = [stat_info.st_size, 1]
while (size[0] > 1024) and (size[1] < 4):
    #size[0] = ceil(size[0] // 1024)
    size[0] = size[0] / 1024
    size[1] += 1
print(f'{ceil(size[0])}{units[size[1]]}')

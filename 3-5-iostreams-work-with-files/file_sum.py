import os

path = '3-5-iostreams-work-with-files/data'
filename = 'numbers_1.num'
numbers = []
with open(os.path.join(path, filename), 'rb') as fin:
    while number := fin.read(2):
        numbers.append(number)
print(sum([int.from_bytes(i, 'big') for i in numbers]) % 2**16)

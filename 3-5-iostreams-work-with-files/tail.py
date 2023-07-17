import os

filename = input()
n_str = int(input())
data_path = '3-5-iostreams-work-with-files/data'
result = [None]*n_str
with open(os.path.join(data_path, filename), 'r', encoding='UTF-8') as fin:
    for line in fin:
        result.append(line)
        result.pop(0)
print(''.join([line for line in result if line is not None]))

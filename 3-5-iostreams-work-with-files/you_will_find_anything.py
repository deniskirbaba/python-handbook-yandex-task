import os
from sys import stdin

query = ''.join(input().lower().split())
files = [filename.rstrip('\n') for filename in stdin.readlines()]
path = '3-5-iostreams-work-with-files/data'
result = []
for idx, filename in enumerate(files):
    with open(os.path.join(path, filename), 'r', encoding='UTF-8') as fin:
        data = fin.read()
    if query in ''.join(data.lower().split()):
        result.append(filename)
if len(result) > 0:
    print('\n'.join(result))
else:
    print('404. File not found')

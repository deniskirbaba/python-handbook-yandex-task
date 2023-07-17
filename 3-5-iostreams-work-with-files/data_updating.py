import os
import json
from sys import stdin

filename = input()
path = '3-5-iostreams-work-with-files/data'

new_data = dict()
for line in stdin:
    key, value = line.split(' == ')
    new_data[key] = value.rstrip('\n')

if len(new_data) > 0:
    with open(os.path.join(path, filename), 'r', encoding='UTF-8') as fin:
        data = json.load(fin)
    data.update(new_data)
    with open(os.path.join(path, filename), 'w', encoding='UTF-8') as fout:
        json.dump(data, fout, indent=4, ensure_ascii=False)

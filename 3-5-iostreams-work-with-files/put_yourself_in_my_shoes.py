import os
import json
from sys import stdin

outputs = [i.strip() for i in stdin.readlines()]

path = '3-5-iostreams-work-with-files/data'
score_filename = 'scoring.json'
with open(os.path.join(path, score_filename), 'r', encoding='UTF-8') as fin:
    scoring = json.load(fin)

final_score = 0
cur_idx = 0
for group in scoring:
    correct = 0
    for test in group['tests']:
        if test['pattern'] == outputs[cur_idx]:
            correct += 1
        cur_idx += 1
    final_score += group['points'] * correct / len(group['tests'])
print(int(final_score))

import os
import json

main_fn = input()
new_fn = input()
path = '3-5-iostreams-work-with-files/data'

with open(os.path.join(path, new_fn), 'r', encoding='UTF-8') as fin:
    new_data = json.load(fin)

assert len(new_data) > 0, 'new data is empty'

with open(os.path.join(path, main_fn), 'r', encoding='UTF-8') as fin:
    old_data = json.load(fin)

result = dict()

for entry in old_data:
    cur_name = entry['name']
    for new_entry in new_data:
        if cur_name == new_entry['name']:
            for key, value in new_entry.items():
                if key not in entry:
                    entry[key] = value
                elif value > entry[key]:
                    entry[key] = value
    del entry['name']
    result[cur_name] = entry

with open(os.path.join(path, main_fn), 'w', encoding='UTF-8') as fout:
    json.dump(result, fout, ensure_ascii=False, indent=4)
    
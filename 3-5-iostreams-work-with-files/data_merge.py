import os
import json

data_filename = input()
new_data_filename = input()
path = '3-5-iostreams-work-with-files/data'

with open(os.path.join(path, new_data_filename), 'r', encoding='UTF-8') as fin:
    new_data = json.load(fin)
if len(new_data) > 0:
    with open(os.path.join(path, data_filename), 'r', encoding='UTF-8') as fin:
        data = json.load(fin)
    changes = False
    for new_entry in new_data:
        for old_entry in data:
            if new_entry['name'] == old_entry['name']:
                for key, value in new_entry.items():
                    if key not in old_entry:
                        old_entry[key] = value
                        changes = True
                    elif value > old_entry[key]:
                        old_entry[key] = value
                        changes = True
    if changes:
        with open(os.path.join(path, data_filename), 'w', encoding='UTF-8') as fout:
            json.dump(data, fout, ensure_ascii=False, indent=4)
    
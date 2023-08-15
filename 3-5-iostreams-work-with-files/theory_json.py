import json

with open('data_54ea06a7cf.json', encoding='UTF-8') as file_in:
    content = json.load(file_in)
print(content)

content[1]['group_number'] = 2
with open('data_54ea06a7cf.json', 'w', encoding='UTF-8') as file_out:
    json.dump(content, file_out, ensure_ascii=False, indent=2)

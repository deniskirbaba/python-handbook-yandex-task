import os

source_file = input()
result_file = input()
data_path = '3-5-iostreams-work-with-files/data'
with open(os.path.join(data_path, source_file), 'r', encoding='UTF-8') as fin:
    fdata = fin.readlines()
result = []
for line in fdata:
    if line != '\n':
        line = line.replace('\t', '')
        result.append(' '.join(line.split()))
with open(os.path.join(data_path, result_file), 'w', encoding='UTF-8') as fout:
    fout.write('\n'.join(result))

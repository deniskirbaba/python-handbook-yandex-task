from sys import stdin
import os

filenames = stdin.readlines()
relative_path = '3-5-iostreams-work-with-files/data'
words = []
for i in range(2):
    words.append(set())
    with open(os.path.join(relative_path, filenames[i].rstrip('\n')), 'r', encoding='UTF-8') as file_in:
        for word in file_in.read().split():
            words[i].add(word)
difference = words[0] ^ words[1]
result = '\n'.join([word for word in sorted(list(difference))])
with open(os.path.join(relative_path, filenames[2]), 'w', encoding='UTF-8') as file_out:
    file_out.write(result)

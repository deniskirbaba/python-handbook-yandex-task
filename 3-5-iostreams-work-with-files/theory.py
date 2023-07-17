from sys import stdin
import os

# lines = []
# for line in stdin:
#     lines.append(line.rstrip('\n'))
# print(lines)

# lines = stdin.readlines()
# print(lines)

# text = stdin.read()
# print([text])

# file_in = open('data.txt', encoding='UTF-8')
# for line in file_in:
#     print(line.rstrip('\n'))
# file_in.close()

# with open('/data/data.txt', encoding='UTF-8') as file_in:
#     for line in file_in:
#         print(line.rstrip('\n'))

# with open('data.txt', encoding='UTF-8') as file_in:
#     lines = file_in.readlines()
# print(lines)

# with open('data.txt', encoding='UTF-8') as file_in:
#     text = file_in.read(10)
# print([text])

# with open('data.txt', 'w', encoding='UTF-8') as file_out:
#     n = file_out.write('new content\nby den')
# print(n)

# lines = ['new content\n', 'by den\n']
# with open('data.txt', 'w', encoding='UTF-8') as file_out:
#     file_out.writelines(lines)

# with open('data.txt', 'w', encoding='UTF-8') as file_out:
#     print('out with print in file\nbyden\n', file=file_out)

print(os.getcwd())
with open('3-5-iostreams-work-with-files/data/cyrillic.txt', 'r', encoding='UTF-8') as file_in:
    print(file_in.read())

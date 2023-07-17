import os


def analyze_digits(n):
    even_count = 0
    odd_count = 0
    while n > 0:
        if (n % 10) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        n = n // 10
    if even_count > odd_count:
        return 'even'
    elif odd_count > even_count:
        return 'odd'
    else:
        return 'eq'


def get_output(d, n_lines):
    out = ''
    for i in range(n_lines):
        if i in d.keys():
            out += ' '.join(d[i])
        out += '\n'
    return out.rstrip('\n')


source = input()
even = input()
odd = input()
eq = input()
path = '3-5-iostreams-work-with-files/data'

with open(os.path.join(path, source), 'r', encoding='UTF-8') as fin:
    data = fin.readlines()

even_n = dict()
odd_n = dict()
eq_n = dict()

for line_idx, line in enumerate(data):
    for number in line.split():
        match analyze_digits(int(number)):
            case 'even':
                even_n.setdefault(line_idx, []).append(number)
            case 'odd':
                odd_n.setdefault(line_idx, []).append(number)
            case 'eq':
                eq_n.setdefault(line_idx, []).append(number)

with open(os.path.join(path, even), 'w', encoding='UTF-8') as fout:
    fout.write(get_output(even_n, len(data)))
with open(os.path.join(path, odd), 'w', encoding='UTF-8') as fout:
    fout.write(get_output(odd_n, len(data)))
with open(os.path.join(path, eq), 'w', encoding='UTF-8') as fout:
    fout.write(get_output(eq_n, len(data)))

from sys import stdin

clean_code = ''
for line in stdin:
    grid_idx = line.find('#')
    if grid_idx > 0:
        clean_code += line[:grid_idx] + '\n'
    elif grid_idx == -1:
        clean_code += line
print(clean_code)

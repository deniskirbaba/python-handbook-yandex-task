req_length = int(input())
n_lines = int(input())

res_heading = ''
cur_length = 3

for i in range(n_lines):
    line = input()
    if cur_length + len(line) < req_length:
        res_heading += line + '\n'
        cur_length += len(line)
    elif cur_length + len(line) == req_length:
        res_heading += line
        cur_length += len(line)
    else:
        res_heading += line[:req_length - cur_length]
        break
    
print(res_heading + '...')
            
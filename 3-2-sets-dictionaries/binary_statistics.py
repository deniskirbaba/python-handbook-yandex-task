numbers = [str(bin(int(i)))[2:] for i in input().split()]

data = []
for i in numbers:
    num_dict = {'digits': len(i), 'units': i.count('1')}
    num_dict['zeros'] = num_dict['digits'] - num_dict['units']
    data.append(num_dict)

print(data)

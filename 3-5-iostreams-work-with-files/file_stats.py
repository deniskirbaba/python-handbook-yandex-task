from sys import stdin
import os

file_name = stdin.readline().strip()
file_path = os.path.join('3-5-iostreams-work-with-files/data', file_name)
numbers = []
with open(file_path, 'r', encoding='UTF-8') as file_in:
    for number in file_in.read().split():
        numbers.append(int(number))
quantity = len(numbers)
quantity_pos = len([i for i in numbers if i > 0])
sum_numbers = sum(numbers)
mean = round(sum_numbers / quantity, 2)
print(f'{quantity}\n{quantity_pos}\n{min(numbers)}\n{max(numbers)}\n{sum_numbers}\n{mean}')
